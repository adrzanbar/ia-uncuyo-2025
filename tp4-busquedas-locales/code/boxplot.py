import os
from pathlib import Path
import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read CSV from current working directory and save outputs to ./images in cwd
CSV_PATH = Path.cwd() / "nqueens_results.csv"
# Update OUT_DIR to include a timestamp
OUT_DIR = Path.cwd() / "images" / datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Define the algorithms to include in the plots
ALGORITHMS = ["HC", "SA", "LGA"]


def ensure_out_dir():
    OUT_DIR.mkdir(parents=True, exist_ok=True)


def read_data(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    # Normalize column names if needed
    df.columns = [c.strip() for c in df.columns]

    # Filter data to include only specified algorithms
    if "algorithm_name" in df.columns:
        df = df[df["algorithm_name"].isin(ALGORITHMS)]
    return df


def create_plots(df: pd.DataFrame):
    ensure_out_dir()

    # Metrics to plot
    metrics = [
        ("H", "H", False),
        ("states", "States Explored", False),
        ("time", "Time (s)", True),
    ]

    # Ensure algorithm_name exists
    if "algorithm_name" not in df.columns:
        raise RuntimeError("CSV missing 'algorithm_name' column")

    # Iterate sizes
    for size in sorted(df["size"].unique()):
        df_size = df[df["size"] == size]
        for metric_key, metric_label, is_time in metrics:
            plt.figure(figsize=(9, 6))

            sns.set_style("whitegrid")
            sns.set_palette("Set2")

            # Put algorithm on the horizontal (categorical) axis and metric on vertical numeric axis
            ax = sns.boxplot(data=df_size, x="algorithm_name", y=metric_key, orient="v")

            ax.set_title(f"{metric_label} by Algorithm (size={size})", fontsize=14)
            ax.set_xlabel("Algorithm", fontsize=12)
            ax.set_ylabel(metric_label, fontsize=12)

            # Rotate algorithm names if they overlap
            plt.xticks(rotation=45)

            # For time metric ensure plain formatting on y-axis
            if is_time:
                ax.ticklabel_format(style="plain", axis="y")

            plt.tight_layout()

            out_file = OUT_DIR / f"boxplot_size-{size}_{metric_key}.png"
            plt.savefig(out_file, dpi=300, bbox_inches="tight")
            print(f"Saved {out_file}")
            plt.close()


def main():
    print(f"Reading CSV from: {CSV_PATH}")
    df = read_data(CSV_PATH)
    create_plots(df)


if __name__ == "__main__":
    main()
