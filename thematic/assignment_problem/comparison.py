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
from scipy.optimize import linear_sum_assignment
from tqdm import tqdm


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
        "-n",
        type=int,
        default=10,
        nargs="+",
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
            start = time.time()
            best_perm = brute_force(cost)
            end = time.time()
            #print(f"Brute force took {end-start:.9f} sec.")
            print(f"Brute force           took {end-start:.9f} sec, i.e. {(end-start)*10**6:,.0f} ms")
            # convert to np.array for easier visual comparison
            #print(f"best_perm = {best_perm}")
            print(f"best_perm =  {np.array(best_perm)}")
            print(f"sum = {cost[range(cost.shape[0]), best_perm].sum()}")
            print()

        start = time.time()
        _, scipy_perm = linear_sum_assignment(cost, maximize=True)
        end = time.time()
        print(f"linear_sum_assignment took {end-start:.9f} sec, i.e. {(end-start)*10**6:,.0f} ms")
        print(f"scipy_perm = {scipy_perm}")
        print(f"sum = {cost[range(cost.shape[0]), scipy_perm].sum()}")
        print()

        start = time.time()
        pulp_perm = pulp_way(cost)
        end = time.time()
        print(f"pulp_way              took {end-start:.9f} sec, i.e. {(end-start)*10**6:,.0f} ms")
        print(f"pulp_perm = {np.array(pulp_perm)}")
        print(f"sum = {cost[range(cost.shape[0]), pulp_perm].sum()}")
        print()


        if show_more:
            start = time.time()
            do_nothing_loop(cost)
            end = time.time()
            print(f"do_nothing_loop() took {end-start:.2f} sec.")
            print()

        # TODO: debug
        # OverflowError: Python int too large to convert to C ssize_t
        if show_more:
            start = time.time()
            do_even_less_loop(cost)
            end = time.time()
            print(f"do_even_less_loop() took {end-start:.2f} sec.")
            print()
