import time
import csv
import os
from search import (
    InstrumentedProblem,
    NQueensProblem,
    hill_climbing,
    simulated_annealing,
    genetic_algorithm,
)

if __name__ == "__main__":
    sizes = [4, 8, 10, 12, 15]
    num_runs = 30
    results = {
        "HC": {4: [], 8: [], 10: [], 12: [], 15: []},
        "SA": {4: [], 8: [], 10: [], 12: [], 15: []},
        "GA": {4: [], 8: [], 10: [], 12: [], 15: []},
        "LGA": {4: [], 8: [], 10: [], 12: [], 15: []},
    }

    for seed in range(num_runs):
        for size in sizes:
            print(f"Running HC with seed {seed} and size {size}")
            problem = InstrumentedProblem(NQueensProblem(size, seed))
            start = time.time()
            solution = hill_climbing(problem)
            end = time.time()
            result = {
                "best_solution": solution,
                "H": problem.value(solution),
                "states": problem.states,
                "time": end - start,
            }
            print(result)
            print()
            results["HC"][size].append(result)

            print(f"Running SA with seed {seed} and size {size}")
            problem = InstrumentedProblem(NQueensProblem(size, seed))
            start = time.time()
            solution = simulated_annealing(problem)
            end = time.time()
            result = {
                "best_solution": solution,
                "H": problem.value(solution),
                "states": problem.states,
                "time": end - start,
            }
            print(result)
            print()
            results["SA"][size].append(result)

            print(f"Running GA with seed {seed} and size {size}")
            problem = InstrumentedProblem(NQueensProblem(size, seed))
            start = time.time()
            solution = genetic_algorithm(problem)
            end = time.time()
            result = {
                "best_solution": solution,
                "H": problem.value(solution),
                "states": problem.states,
                "time": end - start,
            }
            print(result)
            print()
            results["GA"][size].append(result)

            print(f"Running LGA with seed {seed} and size {size}")
            problem = InstrumentedProblem(NQueensProblem(size, seed))
            start = time.time()
            solution = genetic_algorithm(problem, lamarckian=True)
            end = time.time()
            result = {
                "best_solution": solution,
                "H": problem.value(solution),
                "states": problem.states,
                "time": end - start,
            }
            print(result)
            print()
            results["LGA"][size].append(result)

    output_file = os.path.join(
        "/home/adrian/ia-uncuyo-2025/tp4-busquedas-locales", "nqueens_results.csv"
    )
    with open(output_file, "w", newline="") as csvfile:
        fieldnames = [
            "algorithm_name",
            "env_n",
            "size",
            "best_solution",
            "H",
            "states",
            "time",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for algo, sizes_dict in results.items():
            for size, runs in sizes_dict.items():
                for env_n, run in enumerate(runs):
                    writer.writerow(
                        {
                            "algorithm_name": algo,
                            "env_n": env_n,
                            "size": size,
                            "best_solution": run["best_solution"],
                            "H": run["H"],
                            "states": run["states"],
                            "time": run["time"],
                        }
                    )
