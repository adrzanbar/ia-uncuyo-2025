import csv
import random
import statistics
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from csp import (
    NQueensCSP,
    backtracking_search,
    forward_checking,
    no_inference,
    first_unassigned_variable,
    mrv,
    unordered_domain_values,
    lcv,
)

BASE_DIR = Path(__file__).resolve().parent.parent  # tp5-csp/
IMAGES_DIR = BASE_DIR / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

ALGORITHMS = {
    "backtracking_first_unassigned_variable_default_order": {"select": first_unassigned_variable, "order": unordered_domain_values, "inference": no_inference},
    "forward_checking_first_unassigned_variable_default_order": {"select": first_unassigned_variable, "order": unordered_domain_values, "inference": forward_checking},
    "backtracking_first_unassigned_variable_lcv": {"select": first_unassigned_variable, "order": lcv, "inference": no_inference},
    "forward_checking_first_unassigned_variable_lcv": {"select": first_unassigned_variable, "order": lcv, "inference": forward_checking},
    "backtracking_mrv_default_order": {"select": mrv, "order": unordered_domain_values, "inference": no_inference},
    "forward_checking_mrv_default_order": {"select": mrv, "order": unordered_domain_values, "inference": forward_checking},
    "backtracking_mrv_lcv": {"select": mrv, "order": lcv, "inference": no_inference},
    "forward_checking_mrv_lcv": {"select": mrv, "order": lcv, "inference": forward_checking},
}

N_VALUES = [4, 8, 10, 12, 15]
SEEDS = list(range(1, 31))
RESULTS_CSV = BASE_DIR / "tp5-Nreinas.csv"
STATS_CSV = BASE_DIR / "tp5-stats.csv"


def run_once(n, select, order, inference, rng):
    csp = NQueensCSP(n)
    start = time.time()
    result = backtracking_search(
        csp,
        select_unassigned_variable=select,
        order_domain_values=order,
        inference=inference,
    )
    elapsed = time.time() - start
    found = result is not None
    nodes = csp.nassigns
    return found, elapsed, nodes


def run_experiment():
    rows = []
    for algo_name, cfg in ALGORITHMS.items():
        select = cfg["select"]
        order = cfg["order"]
        inference = cfg["inference"]
        for n in N_VALUES:
            for seed in SEEDS:
                rng = random.Random(seed)
                found, elapsed, nodes = run_once(n, select, order, inference, rng)
                rows.append(
                    {
                        "algorithm": algo_name,
                        "n_queens": n,
                        "seed": seed,
                        "found": found,
                        "time_seconds": round(elapsed, 6),
                        "nodes_explored": nodes,
                    }
                )
    return rows


def write_results(rows):
    fields = ["algorithm", "n_queens", "seed", "found", "time_seconds", "nodes_explored"]
    with open(RESULTS_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def compute_stats(rows):
    stats = []
    for algo_name in ALGORITHMS:
        for n in N_VALUES:
            subset = [
                r
                for r in rows
                if r["algorithm"] == algo_name and r["n_queens"] == n
            ]
            found_rows = [r for r in subset if r["found"]]
            found_pct = 100.0 * len(found_rows) / len(subset)
            times = [r["time_seconds"] for r in found_rows] or [0.0]
            nodes = [r["nodes_explored"] for r in found_rows] or [0]
            stats.append(
                {
                    "algorithm": algo_name,
                    "n_queens": n,
                    "found_pct": round(found_pct, 2),
                    "time_mean": round(statistics.mean(times), 6),
                    "time_std": round(statistics.pstdev(times), 6),
                    "nodes_mean": round(statistics.mean(nodes), 2),
                    "nodes_std": round(statistics.pstdev(nodes), 2),
                }
            )
    return stats


def write_stats(stats):
    fields = [
        "algorithm",
        "n_queens",
        "found_pct",
        "time_mean",
        "time_std",
        "nodes_mean",
        "nodes_std",
    ]
    with open(STATS_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(stats)


def print_stats(stats):
    header = (
        f"{'algo':<16}{'n':>4}{'solved%':>9}{'t_mean':>12}"
        f"{'t_std':>12}{'nodes_mean':>12}{'nodes_std':>12}"
    )
    print(header)
    print("-" * len(header))
    for s in stats:
        print(
            f"{s['algorithm']:<16}{s['n_queens']:>4}{s['found_pct']:>9}"
            f"{s['time_mean']:>12}{s['time_std']:>12}"
            f"{s['nodes_mean']:>12}{s['nodes_std']:>12}"
        )


def make_boxplots(rows, metric, title, filename):
    filename = IMAGES_DIR / filename
    fig, axes = plt.subplots(1, len(N_VALUES), figsize=(5 * len(N_VALUES), 5), sharey=False)
    if len(N_VALUES) == 1:
        axes = [axes]
    algo_labels = list(ALGORITHMS.keys())
    colors = {}
    for algo_name in algo_labels:
        if "backtracking" in algo_name and "mrv" in algo_name:
            colors[algo_name] = "tab:green"
        elif "forward_checking" in algo_name and "mrv" in algo_name:
            colors[algo_name] = "tab:red"
        elif "backtracking" in algo_name and "lcv" in algo_name:
            colors[algo_name] = "tab:purple"
        elif "forward_checking" in algo_name and "lcv" in algo_name:
            colors[algo_name] = "tab:cyan"
        elif "backtracking" in algo_name and "default_order" in algo_name:
            colors[algo_name] = "tab:blue"
        elif "forward_checking" in algo_name and "default_order" in algo_name:
            colors[algo_name] = "tab:orange"
    
    short_labels = {}
    for algo_name in algo_labels:
        if "backtracking_first_unassigned_variable_default_order" == algo_name:
            short_labels[algo_name] = "b"
        elif "forward_checking_first_unassigned_variable_default_order" == algo_name:
            short_labels[algo_name] = "fc"
        elif "backtracking_first_unassigned_variable_lcv" == algo_name:
            short_labels[algo_name] = "blcv"
        elif "forward_checking_first_unassigned_variable_lcv" == algo_name:
            short_labels[algo_name] = "fclcv"
        elif "backtracking_mrv_default_order" == algo_name:
            short_labels[algo_name] = "bmrv"
        elif "forward_checking_mrv_default_order" == algo_name:
            short_labels[algo_name] = "fcmrv"
        elif "backtracking_mrv_lcv" == algo_name:
            short_labels[algo_name] = "bmrvlcv"
        elif "forward_checking_mrv_lcv" == algo_name:
            short_labels[algo_name] = "fcmrvlcv"
        else:
            short_labels[algo_name] = algo_name

    for ax, n in zip(axes, N_VALUES):
        data = []
        for algo_name in algo_labels:
            values = [
                r[metric]
                for r in rows
                if r["algorithm"] == algo_name
                and r["n_queens"] == n
                and r["found"]
            ]
            data.append(values)
        bp = ax.boxplot(data, tick_labels=[short_labels[algo] for algo in algo_labels], patch_artist=True)
        for patch, algo_name in zip(bp["boxes"], algo_labels):
            patch.set_facecolor(colors[algo_name])
        ax.set_title(f"{n}-reinas")
        ax.set_ylabel(metric)
        ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle(title)
    fig.tight_layout()
    fig.savefig(filename, dpi=120)
    plt.close(fig)


def main():
    rows = run_experiment()
    write_results(rows)
    stats = compute_stats(rows)
    write_stats(stats)
    print_stats(stats)
    make_boxplots(rows, "time_seconds", "Tiempo de ejecucion (s)", "boxplot_time.png")
    make_boxplots(
        rows, "nodes_explored", "Nodos explorados", "boxplot_nodes.png"
    )
    print(f"\nResultados en {RESULTS_CSV}; estadisticas en {STATS_CSV}")
    print(f"Boxplots: {IMAGES_DIR / 'boxplot_time.png'}, {IMAGES_DIR / 'boxplot_nodes.png'}")


if __name__ == "__main__":
    main()
