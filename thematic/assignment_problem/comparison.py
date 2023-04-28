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
    GLPK,
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
# 4. [ ] real-number linear programming solution, i.e. sth diff from pulp


def do_nothing_bar(*args, **kargs):
    return args[0]


def brute_force_max(R: np.ndarray, *args, verbose: bool = False):
    k = R.shape[0]
    maximum = -np.inf
    #bar = tqdm if verbose else (lambda iterator, total: iterator)
    bar = tqdm if verbose else do_nothing_bar
    for perm in bar(permutations(range(k)), total=np.math.factorial(k)):
        somme = R[range(k), perm].sum()
        if somme >= maximum:
            maximum = somme
            best_perm = perm
    return best_perm


def brute_force(R: np.ndarray, *args, verbose: bool = False, minimize: bool = False):
    if minimize:
        return brute_force_max(-R, verbose=verbose)
    else:
        return brute_force_max(R, verbose=verbose)


def pulp_way(R, *args, minimize=False, solver=GLPK, debug=False):
    m, n = R.shape
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
        model += (lpSum(X[i][j] for i in range(m)) == 1, f"col_{j}_sum")
    obj_func = lpSum(
        R[i,j]*X[i][j] for i in range(m) for j in range(n)
    )
    model += obj_func
    status = model.solve(solver=solver(msg=False))
    if debug:
        print(f"{model.objective.value() = }")
    perm = []
    for k, var in enumerate(model.variables()):
        if debug:
            print(f"{var.name} = {var.value()}")
        if var.value() == 1:
            j = k % n
            perm.append(j)
    #print(f"{perm = }")
    return perm


def do_nothing_loop(R):
    k = R.shape[0]
    for _ in tqdm(permutations(range(k)), total=np.math.factorial(k)):
        pass


def do_even_less_loop(R):
    k = R.shape[0]
    k_factorial = np.math.factorial(k)
    for _ in tqdm(range(k_factorial), total=k_factorial):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "n",
        type=int,
        default=10,
        nargs="*",
        help="number of rows/cols of the rating/cost matrix",
    )
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
    print(f"args.n = {args.n}")
    n = args.n if isinstance(args.n, list) else [args.n]
    seed = args.seed
    sum_name = "min_cost_sum" if args.minimize else "max_rating_sum"
    perm_name_decalage = 21

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
        perm_name = "brute_force_perm"
        start = time.perf_counter()
        brute_force_perm = brute_force(
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
        #width_sec = len(str(int(duration)))
        #print(f"Brute force      took {duration: {width_sec}.9f} sec, i.e. {(duration)*10**6:,.0f} ms")
        print(f"took {sec_str} sec, i.e. {ms_str} ms")

        # convert to np.array for easier visual comparison
        #print(f"brute_force_perm = {brute_force_perm}")
        print(f"{perm_name:<{perm_name_decalage}} = {np.array(brute_force_perm)}")
        print(f"{sum_name} = {R[range(R.shape[0]), brute_force_perm].sum()}")
        print()

    #print("PuLP:")
    #perm_name = "pulp_perm"
    #start = time.perf_counter()
    ## TODO: Other solvers than GLPK?
    #pulp_perm = pulp_way(
    #    R,
    #    minimize=args.minimize,
    #    solver=GLPK,
    #    debug=False,
    #)
    #end = time.perf_counter()
    #duration = end - start
    #sec_str = f"{duration:.9f}"
    #ms_str = f"{(duration)*10**6:,.0f}"
    #if args.no_brute_force:
    #    n_char_sec = len(sec_str)
    #    n_char_ms = len(ms_str)

    #print(f'took {sec_str:>{n_char_sec}} sec, i.e. {ms_str:>{n_char_ms}} ms')
    #print(f'{perm_name:<{perm_name_decalage}} = {np.array(pulp_perm)}')
    #print(f'{sum_name} = {R[range(R.shape[0]), pulp_perm].sum()}')
    #print()

    print("Hungarian:")
    perm_name = "kuhn_munkres_perm "
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
    print(f"{perm_name:<{perm_name_decalage}} = {hungarian_assign}")
    print(f"{sum_name} = {R[row_ind, col_ind].sum()}", end="")
    for i, (row, col) in enumerate(hungarian_assign):
        v = R[row, col]
        if i == 0:
            print(f' = {v}', end="")
        else:
            print(f' + {v}', end="")
    print()

    print("Jonker-Volgenant:")
    perm_name = "jonker_volgenant_perm"
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
    print(f"{perm_name:<{perm_name_decalage}} = {jv_assign}")
    print(f"{sum_name} = {R[row_ind, col_ind].sum()}", end="")
    for i, (row, col) in enumerate(jv_assign):
        v = R[row, col]
        if i == 0:
            print(f' = {v}', end="")
        else:
            print(f' + {v}', end="")
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
