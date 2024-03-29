from __future__ import annotations
import argparse
from itertools import permutations, combinations
import math
import time

import numpy as np
from pulp import (
    LpProblem,
    LpVariable,
    LpMaximize,
    LpMinimize,
    lpSum,
    listSolvers,
    getSolver,
)
from scipy.optimize import linear_sum_assignment as jonker_volgenant
from tqdm import tqdm
from _hungarian import linear_sum_assignment as kuhn_munkres


# TODO:
# 1. [ ] Change the behavior of this script to allow
#    non-square matrix input for all of the functions:
#    brute_force, pulp_way, etc.
#    Default: square matrix, allow non-square
# 2. [x] Allow minimization as well as maximization
# 3. [x] Prettier formated printing
# 4. [ ] real-number linear programming solution, i.e. sth diff from pulp, e.g. scipy
# 5. [ ] np.int64 integer overflow consideration: Convert all matrices to dtype=float


def do_nothing_bar(*args, **kargs):
    return args[0]


def brute_force(R: np.ndarray | list, *args, verbose: bool = False, minimize: bool = False):
    if isinstance(R, list):
        R = np.array(R)

    if minimize:
        return brute_force_max(-R, verbose=verbose)
    else:
        return brute_force_max(R, verbose=verbose)


def brute_force_max(R: np.ndarray, *args, verbose: bool = False):
    m, n = get_matrix_shape(R)
    if m <= n:
        row_ind, col_ind = brute_force_fat_max(R, verbose=verbose)
    else:
        col_ind, row_ind = brute_force_fat_max(R.T, verbose=verbose)
    return row_ind, col_ind


def get_matrix_shape(R: np.ndarray):
    try:
        m, n = R.shape
    except AttributeError as e:
        msg = f"Expect R to be an np.ndarray, but got {type(R) = }"
        e.args = (msg,)
        raise e
    except ValueError as e:
        msg = f"Expect R to be an np.ndarray with ndim=2, but got {R.shape = }"
        e.args = (msg,)
        raise e
    return m, n


def brute_force_fat_max(R: np.ndarray, *args, verbose: bool = False):
    """
    Def. R is said to be fat iff (R.ndim == 2 and R.shape[1] >= R.shape[0])
    """
    m, n = R.shape
    assert n >= m, f'Expect n >= m, but got {(m, n) = }'
    row_ind = tuple(range(m))

    # Convert dtype to float to avoid int overflow in NumPy
    if not np.issubdtype(R.dtype, np.floating):
        R = R.astype(np.float64)

    bar = tqdm if verbose else do_nothing_bar
    maximum = -np.inf

    #for comb in bar(combinations(range(n), m)):
    #    for perm in permutations(comb):
    #        pass

    # `permutations` alone could achieve the above double for-loop
    total = np.product(range(n, n-m, -1))
    for col_ind in bar(permutations(range(n), m), total=total):
        somme = R[row_ind, col_ind].sum()
        if somme >= maximum:
            maximum = somme
            best_col_ind = col_ind
    return row_ind, best_col_ind


def pulp_way(R, *args, minimize=False, solver: None|str =None, debug=False):
    m, n = get_matrix_shape(R)

    if m <= n:
        row_ind, col_ind = pulp_fat(R, minimize=minimize,
                                    solver=solver, debug=debug)
    else:
        col_ind, row_ind = pulp_fat(R.T, minimize=minimize,
                                    solver=solver, debug=debug)
    return row_ind, col_ind


def pulp_fat(R, *args, minimize=False, solver: None|str =None, debug=False):
    m, n = R.shape
    assert n >= m, f'Expect n >= m, but got {(m, n) = }'
    row_ind = tuple(range(m))

    # Convert dtype to float to avoid int overflow in NumPy
    if not np.issubdtype(R.dtype, np.floating):
        R = R.astype(np.float64)

    sense = LpMinimize if minimize else LpMaximize
    model = LpProblem(name="linear-assignment", sense=sense)
    X = []
    for i in range(m):
        X.append([])
        for j in range(n):
            X[i].append(
                LpVariable(name=f"X[{i},{j}]", cat="Binary")
            )
    # Constraints
    for i in range(m):
        model += (lpSum(X[i]) == 1, f"row_{i}_sum")
    for j in range(n):
        model += (lpSum(X[i][j] for i in range(m)) <= 1, f"col_{j}_sum_ceiling")
        #model += (lpSum(X[i][j] for i in range(m)) >= 0, f"col_{j}_sum_floor")
    obj_func = lpSum(
        R[i,j]*X[i][j] for i in range(m) for j in range(n)
    )
    model += obj_func
    available_solvers = listSolvers(onlyAvailable=True)
    if solver is None:
        solver = getSolver(np.random.choice(available_solvers), msg=False)
    elif isinstance(solver, str):
        if solver not in available_solvers:
            msg = f'Valid solver strings include {available_solvers}, but got invalid "{solver}"'
            raise ValueError(msg)
        solver = getSolver(solver, msg=False)
    else:
        msg = f'solver expected to have type str or be None, but got {type(solver) = }'
        raise TypeError(msg)
    status = model.solve(solver=solver)
    if debug:
        print(f'{status = }')
        print(f"{model.objective.value() = }")
    col_ind = []
    for k, var in enumerate(model.variables()):
        if debug:
            print(f"{var.name} = {var.value()}")
        if var.value() == 1:
            j = k % n
            col_ind.append(j)
    return row_ind, col_ind


def do_nothing_loop(R: np.ndarray):
    m, n = get_matrix_shape(R)
    p, q = min(m,n), max(m,n)
    total = np.product(range(q, q-p, -1))
    for _ in tqdm(permutations(range(q), p), total=total):
        pass


def do_even_less_loop(R: np.ndarray):
    m, n = get_matrix_shape(R)
    p, q = min(m,n), max(m,n)
    total = np.product(range(q, q-p, -1))
    for _ in tqdm(range(total), total=total):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--rows",
        type=int,
        default=10,
        help="(# rows) of the rating/cost matrix",
    )
    parser.add_argument(
        "-n",
        "--cols",
        type=int,
        help="(# cols) of the rating/cost matrix",
    )
    parser.add_argument(
        "--no_brute_force",
        action="store_true",
        help="Whether or not to run brute_force()",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="seed for the random rating/cost matrix",
    )
    parser.add_argument(
        "--show_more",
        action="store_true",
        help="show do_nothing_loop() and do_even_less_loop()",
    )
    parser.add_argument(
        "--minimize",
        default=False,
        action="store_true",
        help="Either to maximize (rating sum) or to minimize (cost sum)",
    )
    args = parser.parse_args()
    seed = args.seed
    sum_name = "min_cost_sum" if args.minimize else "max_rating_sum"
    assign_name_decalage = len("jonker_volgenant_assign")

    if not isinstance(args.rows, int):
        print(
            f'{args.rows = } is of invalid type {type(args.rows)}. '
            "Please specify --rows with a positive integer."
        )
        return
    elif args.rows <= 0:
        print(
            f'{args.rows = } is non-positive.'
            "Please specify --rows with a positive integer."
        )
        return

    if not isinstance(args.cols, int):
        args.cols = args.rows

    m, n = args.rows, args.cols
    rng = np.random.default_rng(seed=seed)
    R = rng.integers(low=1, high=10, size=(m,n))
    #R = rng.integers(low=-2**20, high=2**20, size=(k,k))
    print(f"{m}-by-{n} R = \n{R}")
    print()

    if not args.no_brute_force:
        print("Brute Force:")
        assign_name = "brute_force_assign"
        start = time.perf_counter()
        row_ind, col_ind = brute_force(
            R,
            verbose=True,
            minimize=args.minimize,
        )
        end = time.perf_counter()
        duration = end - start
        sec_str = f"{duration:.9f}"
        ms_str = f"{(duration)*10**6:,.0f}"
        n_char_sec = len(sec_str)
        n_char_ms = len(ms_str)
        print(f"took {sec_str} sec, i.e. {ms_str} ms")
        bf_assign = list(zip(row_ind, col_ind))
        print(f"{assign_name:<{assign_name_decalage}} = {bf_assign}")
        print(f"{sum_name} = {R[row_ind, col_ind].sum()}", end="")
        for i, (row, col) in enumerate(bf_assign):
            v = R[row, col]
            if i == 0:
                print(f' = {v}', end="")
            else:
                print(f' + {v}', end="")
        print()
        print()

    print("PuLP:")
    assign_name = "pulp_assign"
    start = time.perf_counter()
    # TODO: Other solvers than the default one and GLPK?
    row_ind, col_ind = pulp_way(
        R,
        minimize=args.minimize,
        solver=None,
        #solver="GLPK_CMD",
        debug=False,
    )
    end = time.perf_counter()
    duration = end - start
    sec_str = f"{duration:.9f}"
    ms_str = f"{(duration)*10**6:,.0f}"
    if args.no_brute_force:
        n_char_sec = len(sec_str)
        n_char_ms = len(ms_str)

    pulp_assign = list(zip(row_ind, col_ind))
    print(f'took {sec_str:>{n_char_sec}} sec, i.e. {ms_str:>{n_char_ms}} ms')
    print(f'{assign_name:<{assign_name_decalage}} = {pulp_assign}')
    print(f'{sum_name} = {R[row_ind, col_ind].sum()}', end="")
    for i, (row, col) in enumerate(pulp_assign):
        v = R[row, col]
        if i == 0:
            print(f' = {v}', end="")
        else:
            print(f' + {v}', end="")
    print()
    print()

    print("Hungarian:")
    assign_name = "kuhn_munkres_assign "
    start = time.perf_counter()
    if args.minimize:
        row_ind, col_ind = kuhn_munkres(R)
    else:
        row_ind, col_ind = kuhn_munkres(-R)
    end = time.perf_counter()
    duration = end - start
    sec_str = f"{duration:.9f}"
    ms_str = f"{(duration)*10**6:,.0f}"
    if "n_char_ms" not in locals() or "n_char_ms" not in locals():
        n_char_sec = len(sec_str)
        n_char_ms = len(ms_str)
    print(f"took {sec_str:>{n_char_sec}} sec, i.e. {ms_str:>{n_char_ms}} ms")
    hungarian_assign = list(zip(row_ind, col_ind))
    print(f"{assign_name:<{assign_name_decalage}} = {hungarian_assign}")
    print(f"{sum_name} = {R[row_ind, col_ind].sum()}", end="")
    for i, (row, col) in enumerate(hungarian_assign):
        v = R[row, col]
        if i == 0:
            print(f' = {v}', end="")
        else:
            print(f' + {v}', end="")
    print()
    print()

    print("Jonker-Volgenant:")
    assign_name = "jonker_volgenant_assign"
    start = time.perf_counter()
    row_ind, col_ind = jonker_volgenant(R, maximize=not args.minimize)
    end = time.perf_counter()
    duration = end - start
    sec_str = f"{duration:.9f}"
    ms_str = f"{(duration)*10**6:,.0f}"
    if "n_char_ms" not in locals() or "n_char_ms" not in locals():
        n_char_sec = len(sec_str)
        n_char_ms = len(ms_str)
    print(f"took {sec_str:>{n_char_sec}} sec, i.e. {ms_str:>{n_char_ms}} ms")
    jv_assign = list(zip(row_ind, col_ind))
    print(f"{assign_name:<{assign_name_decalage}} = {jv_assign}")
    print(f"{sum_name} = {R[row_ind, col_ind].sum()}", end="")
    for i, (row, col) in enumerate(jv_assign):
        v = R[row, col]
        if i == 0:
            print(f' = {v}', end="")
        else:
            print(f' + {v}', end="")
    print()
    print()

    if args.show_more:
        print("do_nothing_loop:")
        start = time.perf_counter()
        do_nothing_loop(R)
        end = time.perf_counter()
        duration = end - start
        sec_str = f"{duration:.9f}"
        ms_str = f"{(duration)*10**6:,.0f}"
        print(f'took {sec_str:>{n_char_sec}} sec, i.e. {ms_str:>{n_char_ms}} ms')
        print()

    # TODO: debug
    # OverflowError: Python int too large to convert to C ssize_t
    if args.show_more:
        print(f"do_even_less_loop:")
        start = time.perf_counter()
        do_even_less_loop(R)
        end = time.perf_counter()
        duration = end - start
        sec_str = f"{duration:.9f}"
        ms_str = f"{(duration)*10**6:,.0f}"
        print(f'took {sec_str:>{n_char_sec}} sec, i.e. {ms_str:>{n_char_ms}} ms')
        print()


if __name__ == "__main__":
    main()
