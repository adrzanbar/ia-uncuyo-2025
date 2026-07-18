import csv
import statistics
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent  # tp4-busquedas-locales/
CSV_PATH = BASE_DIR / "tp4-Nreinas.csv"
STATS_CSV = BASE_DIR / "tp4-stats.csv"
IMAGES_DIR = BASE_DIR / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

ALGORITHMS = ["HC", "SA", "GA", "LGA"]
SHORT_LABELS = {"HC": "hc", "SA": "sa", "GA": "ga", "LGA": "lga"}
COLORS = {"HC": "tab:blue", "SA": "tab:orange", "GA": "tab:green", "LGA": "tab:red"}

METRICS = [
    ("H", "Valor de la heuristica H", "H"),
    ("states", "Estados explorados", "states"),
    ("time", "Tiempo de ejecucion (s)", "time_seconds"),
]

SIZES = [4, 8, 10, 12, 15]


def read_data(csv_path):
    rows = []
    with open(csv_path, newline="") as f:
        for r in csv.DictReader(f):
            if r["algorithm_name"] in ALGORITHMS and int(r["size"]) in SIZES:
                rows.append(
                    {
                        "algorithm": r["algorithm_name"],
                        "size": int(r["size"]),
                        "H": float(r["H"]),
                        "states": float(r["states"]),
                        "time": float(r["time"]),
                    }
                )
    return rows


def make_boxplots(rows, metric, title, filename):
    fig, axes = plt.subplots(1, len(SIZES), figsize=(5 * len(SIZES), 5), sharey=False)
    if len(SIZES) == 1:
        axes = [axes]
    for ax, n in zip(axes, SIZES):
        data = []
        for algo in ALGORITHMS:
            values = [
                r[metric]
                for r in rows
                if r["algorithm"] == algo and r["size"] == n
            ]
            data.append(values)
        bp = ax.boxplot(data, tick_labels=[SHORT_LABELS[a] for a in ALGORITHMS], patch_artist=True)
        for patch, algo in zip(bp["boxes"], ALGORITHMS):
            patch.set_facecolor(COLORS[algo])
        ax.set_title(f"{n}-reinas")
        ax.set_ylabel(metric)
        ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle(title)
    fig.tight_layout()
    fig.savefig(IMAGES_DIR / filename, dpi=120)
    plt.close(fig)
    print(f"Guardado: {IMAGES_DIR / filename}")


def compute_stats(rows):
    stats = []
    for algo in ALGORITHMS:
        for n in SIZES:
            subset = [r for r in rows if r["algorithm"] == algo and r["size"] == n]
            if not subset:
                continue
            max_pairs = n * (n - 1) // 2  # solved board has H == max_pairs
            solved = [r for r in subset if r["H"] == max_pairs]
            solved_pct = 100.0 * len(solved) / len(subset)
            times = [r["time"] for r in subset]
            states = [r["states"] for r in subset]
            hs = [r["H"] for r in subset]
            stats.append(
                {
                    "algorithm": algo,
                    "n_queens": n,
                    "solved_pct": round(solved_pct, 2),
                    "time_mean": round(statistics.mean(times), 6),
                    "time_std": round(statistics.pstdev(times), 6),
                    "states_mean": round(statistics.mean(states), 2),
                    "states_std": round(statistics.pstdev(states), 2),
                    "H_mean": round(statistics.mean(hs), 4),
                    "H_std": round(statistics.pstdev(hs), 4),
                }
            )
    return stats


def write_stats(stats):
    fields = [
        "algorithm",
        "n_queens",
        "solved_pct",
        "time_mean",
        "time_std",
        "states_mean",
        "states_std",
        "H_mean",
        "H_std",
    ]
    with open(STATS_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(stats)


def main():
    rows = read_data(CSV_PATH)
    for col, title, fname in METRICS:
        make_boxplots(rows, col, title, f"boxplot_{fname}.png")
    stats = compute_stats(rows)
    write_stats(stats)
    print(f"\nDatos: {CSV_PATH}")
    print(f"Boxplots en: {IMAGES_DIR}")
    print(f"Estadisticas en: {STATS_CSV}")


if __name__ == "__main__":
    main()
