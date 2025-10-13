import sys
from search import (
    NQueensProblem,
    hill_climbing,
    simulated_annealing,
    genetic_search,
    exp_schedule,
)

if __name__ == "__main__":
    N = 8

    problem = NQueensProblem(N)

    solution = hill_climbing(problem)
    print("Hill Climbing:")
    print("Solution found:", solution)
    print("Number of conflicting queens:", problem.num_conflicts(solution))
    print()

    solution = simulated_annealing(
        # problem, exp_schedule(k=2 * N, lam=1 / N, limit=2 * N * N)
        problem,
        exp_schedule(lam=1 / N, limit=1000),
    )
    print("Simulated Annealing:")
    print("Solution found:", solution)
    print("Number of conflicting queens:", problem.num_conflicts(solution))
    print()

    solution = genetic_search(
        # problem, ngen=10 * N * N, n=2 * N
        problem
    )
    print("Genetic Algorithm:")
    print("Solution found:", solution)
    print("Number of conflicting queens:", problem.num_conflicts(solution))
    print()

    N = 15

    problem = NQueensProblem(N)

    solution = hill_climbing(problem)
    print("Hill Climbing:")
    print("Solution found:", solution)
    print("Number of conflicting queens:", problem.num_conflicts(solution))
    print()

    solution = simulated_annealing(
        # problem, exp_schedule(k=2 * N, lam=1 / N, limit=2 * N * N)
        problem,
        exp_schedule(lam=1 / N),
    )
    print("Simulated Annealing:")
    print("Solution found:", solution)
    print("Number of conflicting queens:", problem.num_conflicts(solution))
    print()

    solution = genetic_search(
        # problem, ngen=10 * N * N, n=2 * N
        problem
    )
    print("Genetic Algorithm:")
    print("Solution found:", solution)
    print("Number of conflicting queens:", problem.num_conflicts(solution))
    print()
