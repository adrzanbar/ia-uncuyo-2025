import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def create_individual_boxplots():
    """Create individual boxplot files for each metric with environments grouped by algorithm"""
    # Read the CSV data
    df = pd.read_csv("/workspaces/ia-uncuyo-2025/frozen_lake_results.csv")

    # Filter out random algorithm as it's out of scale
    df = df[df["algorithm_name"] != "random"]

    # Set up the plotting style
    plt.style.use("default")
    sns.set_palette("Set2")

    # Define the metrics to plot
    metrics = ["states_n", "actions_count", "actions_cost", "time"]
    metric_labels = [
        "States Explored",
        "Actions Count",
        "Actions Cost",
        "Time (seconds)",
    ]

    for metric, label in zip(metrics, metric_labels):
        plt.figure(figsize=(12, 8))

        # Create boxplot with environment as hue (creates side-by-side boxes)
        sns.boxplot(data=df, x="algorithm_name", y=metric, hue="environment")

        # Customize the plot
        plt.title(
            f"{label} by Algorithm and Environment", fontsize=16, fontweight="bold"
        )
        plt.xlabel("Algorithm", fontsize=14)
        plt.ylabel(label, fontsize=14)

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)

        # Add grid for better readability
        plt.grid(True, alpha=0.3)

        # Format y-axis for time metric
        if metric == "time":
            plt.ticklabel_format(style="plain", axis="y")

        # Customize legend
        plt.legend(title="Environment", title_fontsize=12, fontsize=11)

        # Adjust layout
        plt.tight_layout()

        # Save individual plot
        filename = f"/workspaces/ia-uncuyo-2025/tp3-algoritmos-busqueda/code/boxplot_{metric}.png"
        plt.savefig(filename, dpi=300, bbox_inches="tight")
        print(f"Saved {filename}")

        plt.close()

    # Show basic statistics
    print("\nBasic Statistics Summary:")
    print("=" * 50)

    for metric in metrics:
        print(f"\n{metric.upper()}:")
        stats = df.groupby(["environment", "algorithm_name"])[metric].agg(
            ["count", "mean", "std", "min", "max"]
        )
        print(stats.round(4))


if __name__ == "__main__":
    print("Creating individual boxplots with environment comparison...")
    create_individual_boxplots()
    print("\nAll plots have been generated successfully!")
