import time
import csv
import os
import matplotlib.pyplot as plt
from search import (
    InstrumentedProblem,
    NQueensProblem,
    hill_climbing,
    simulated_annealing,
    genetic_algorithm,
)


def run_hill_climbing(size, seed):
    problem = InstrumentedProblem(NQueensProblem(size, seed))
    print(f"Initial state: {problem.initial}")
    solution = hill_climbing(problem)
    print(f"Final state: {solution}")
    print(f"Final H: {problem.value(solution)}")
    print(f"States visited: {problem.states}")
    print(f"States visited: {len(problem.h_series)}")
    return problem.h_series


def run_simulated_annealing(size, seed):
    problem = InstrumentedProblem(NQueensProblem(size, seed))
    print(f"Initial state: {problem.initial}")
    solution = simulated_annealing(problem)
    print(f"Final state: {solution}")
    print(f"Final H: {problem.value(solution)}")
    print(f"States visited: {problem.states}")
    print(f"States visited: {len(problem.h_series)}")
    return problem.h_series


def run_genetic_algorithm(size, seed, elitism=False, lamarckian=False):
    problem = InstrumentedProblem(NQueensProblem(size, seed))
    print(f"Initial state: {problem.initial}")
    solution = genetic_algorithm(problem, elitism=elitism, lamarckian=lamarckian)
    print(f"Final state: {solution}")
    print(f"Final H: {problem.value(solution)}")
    print(f"States visited: {problem.states}")
    print(f"States visited: {len(problem.h_series)}")
    return problem.h_series


def run_full_experiment(sizes, num_runs, output_file):
    results = {
        "HC": {size: [] for size in sizes},
        "SA": {size: [] for size in sizes},
        "GA": {size: [] for size in sizes},
        "LGA": {size: [] for size in sizes},
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
            results["SA"][size].append(result)

            print(f"Running GA with seed {seed} and size {size}")
            problem = InstrumentedProblem(NQueensProblem(size, seed))
            start = time.time()
            solution = genetic_algorithm(problem, elitism=True)
            end = time.time()
            result = {
                "best_solution": solution,
                "H": problem.value(solution),
                "states": problem.states,
                "time": end - start,
            }
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
            results["LGA"][size].append(result)

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


def plot_h_series(h_series):
    plt.figure(figsize=(10, 6))
    for algo, series in h_series.items():
        plt.plot(range(len(series)), series, label=algo)
    plt.xlabel("Iteration")
    plt.ylabel("H Value")
    plt.title("H Series for N-Queens Problem")
    plt.legend()
    plt.grid()
    plt.show()


def plot_h_series_and_save(h_series, output_file):
    plt.figure(figsize=(10, 6))
    for algo, series in h_series.items():
        plt.plot(range(len(series)), series, label=algo)
    plt.xlabel("Iteration")
    plt.ylabel("H Value")
    plt.title("H Series for N-Queens Problem")
    plt.legend()
    plt.grid()
    plt.savefig(output_file)
    plt.close()


if __name__ == "__main__":
    size = 15
    seed = 30
    h_series = {}

    # Run experiments
    # h_series["HC"] = run_hill_climbing(size, seed)
    # h_series["SA"] = run_simulated_annealing(size, seed)
    h_series["GA"] = run_genetic_algorithm(size, seed, elitism=True)
    # h_series["LGA"] = run_genetic_algorithm(size, seed, lamarckian=True)

    # Save plot to file
    output_image = os.path.join(
        f"/home/adrian/ia-uncuyo-2025/tp4-busquedas-locales/images",
        f"nqueens_h_series_plot_{time.time()}.png",
    )
    plot_h_series_and_save(h_series, output_image)

    # sizes = [4, 8, 10, 12, 15]
    # num_runs = 30
    # output_file = os.path.join(
    #     "/home/adrian/ia-uncuyo-2025/tp4-busquedas-locales",
    #     "nqueens_HC_SA_GA_LGA_results.csv",
    # )
    # run_full_experiment(sizes, num_runs, output_file)
