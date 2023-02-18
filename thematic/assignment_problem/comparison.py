import argparse
from itertools import permutations, combinations
import math
import time

import numpy as np
from pulp import (
    LpProblem,
    LpVariable,
    LpMaximize,
    lpSum,
    GLPK,
)
from scipy.optimize import linear_sum_assignment as jonker_volgenant
from tqdm import tqdm
from _hungarian import linear_sum_assignment as kuhn_munkres


# TODO:
# 1. Change the behavior of this script to allow
#    non-square matrix input for all of the functions:
#    brute_force, pulp_way, etc.
#    Default: square matrix, allow non-square
# 2. Prettier formated printing


def brute_force(cost):
    k = cost.shape[0]
    maximum = -np.inf
    #for perm in permutations(range(k)):
    for perm in tqdm(permutations(range(k)), total=np.math.factorial(k)):
        #import ipdb; ipdb.set_trace()
        somme = cost[range(k), perm].sum()
        if somme >= maximum:
            maximum = somme
            best_perm = perm
    return best_perm


def pulp_way(cost, *, verbose=False, solver=GLPK, debug=False):
    m, n = cost.shape
    model = LpProblem(name="linear-assignment", sense=LpMaximize)
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
        cost[i,j]*X[i][j] for i in range(m) for j in range(n)
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


def do_nothing_loop(cost):
    k = cost.shape[0]
    for _ in tqdm(permutations(range(k)), total=np.math.factorial(k)):
        pass


def do_even_less_loop(cost):
    k = cost.shape[0]
    #for _ in tqdm(range(math.factorial(k))):
    for _ in tqdm(range(np.math.factorial(k)), total=np.math.factorial(k)):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "n",
        type=int,
        default=10,
        nargs="?",
        help="number of rows/cols of the cost matrix",
    )
    parser.add_argument(
        "-d",
        "--deactivate",
        action="store_true",
        help="deactivate brute_force()",
    )
    parser.add_argument(
        "--show_more",
        action="store_true",
        help="show do_nothing_loop() and do_even_less_loop()",
    )
    args = parser.parse_args()
    deactivate = args.deactivate
    print(f"args.n = {args.n}")
    n = args.n if isinstance(args.n, list) else [args.n]
    show_more = args.show_more

    for k in n:
        rng = np.random.default_rng(seed=42)
        cost = rng.integers(low=1, high=10, size=(k,k))
        print(f"{k}-by-{k} cost = \n{cost}")
        print()

        if not deactivate:
            start = time.perf_counter()
            brute_force_perm = brute_force(cost)
            end = time.perf_counter()
            duration = end - start
            sec_str = f"{duration:.9f}"
            ms_str = f"{(duration)*10**6:,.0f}"
            n_char_sec = len(sec_str)
            n_char_ms = len(ms_str)
            #width_sec = len(str(int(duration)))
            #print(f"Brute force      took {duration: {width_sec}.9f} sec, i.e. {(duration)*10**6:,.0f} ms")
            print(f"Brute force      took {sec_str} sec, i.e. {ms_str} ms")

            # convert to np.array for easier visual comparison
            #print(f"brute_force_perm = {brute_force_perm}")
            print(f"brute_force_perm =  {np.array(brute_force_perm)}")
            print(f"max_rating_sum = {cost[range(cost.shape[0]), brute_force_perm].sum()}")
            print()

        start = time.perf_counter()
        pulp_perm = pulp_way(cost)
        end = time.perf_counter()
        duration = end - start
        sec_str = f"{duration:.9f}"
        ms_str = f"{(duration)*10**6:,.0f}"
        if deactivate:
            n_char_sec = len(sec_str)
            n_char_ms = len(ms_str)
            #width_sec = len(str(int(duration)))

        #print(f"pulp_way         took {duration: {width_sec}.9f} sec, i.e. {(duration)*10**6:,.0f} ms")
        print(f"pulp_way         took {sec_str:>{n_char_sec}} sec, i.e. {ms_str:>{n_char_ms}} ms")
        print(f"pulp_perm =  {np.array(pulp_perm)}")
        print(f"max_rating_sum = {cost[range(cost.shape[0]), pulp_perm].sum()}")
        print()

        start = time.perf_counter()
        # We need to add a negative sign because
        # _hungarian.py computes the min cost of a cost matrix
        # instead of the max rating sum of a rating matrix
        row_ind, col_ind = kuhn_munkres(-cost)
        end = time.perf_counter()
        duration = end - start
        sec_str = f"{duration:.9f}"
        ms_str = f"{(duration)*10**6:,.0f}"
        #print(f"kuhn_munkres     took {duration: {width_sec}.9f} sec, i.e. {(duration)*10**6:,.0f} ms")
        print(f"kuhn_munkres     took {sec_str:>{n_char_sec}} sec, i.e. {ms_str:>{n_char_ms}} ms")
        #print(f"{row_ind = }")
        #print(f"{col_ind = }")
        print(f"kuhn_munkres_perm = {col_ind}")
        print(f"max_rating_sum = {cost[row_ind, col_ind].sum()}")
        print()

        start = time.perf_counter()
        _, scipy_perm = jonker_volgenant(cost, maximize=True)
        end = time.perf_counter()
        duration = end - start
        sec_str = f"{duration:.9f}"
        ms_str = f"{(duration)*10**6:,.0f}"
        #print(f"jonker_volgenant took {duration: {width_sec}.9f} sec, i.e. {(duration)*10**6:,.0f} ms")
        print(f"jonker_volgenant took {sec_str:>{n_char_sec}} sec, i.e. {ms_str:>{n_char_ms}} ms")
        print(f"scipy_perm = {scipy_perm}")
        print(f"max_rating_sum = {cost[range(cost.shape[0]), scipy_perm].sum()}")
        print()

        if show_more:
            start = time.perf_counter()
            do_nothing_loop(cost)
            end = time.perf_counter()
            print(f"do_nothing_loop() took {end-start:.2f} sec.")
            print()

        # TODO: debug
        # OverflowError: Python int too large to convert to C ssize_t
        if show_more:
            start = time.perf_counter()
            do_even_less_loop(cost)
            end = time.perf_counter()
            print(f"do_even_less_loop() took {end-start:.2f} sec.")
            print()
