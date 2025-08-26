import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_DIR = "./game_data"
FILE_NAME = "simplereflexagent.json"
HEADER = [
    "agent_type",
    "environment_size",
    "dirt_rate",
    "total_dirt_cells",
    "timestamp",
    "server_url",
    "environment_id",
    "final_performance",
    "total_actions",
    "successful_actions",
    "completion_reason",
    "steps_to_completion",
]


def extract_metadata(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
        meta = data["metadata"]
        row = {}
        for key in HEADER:
            if key == "environment_size":
                row[key] = meta.get("environment_size", [None])[0]
            else:
                row[key] = meta.get(key, None)
        return row


def main():
    rows = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(FILE_NAME):
            path = os.path.join(DATA_DIR, filename)
            try:
                row = extract_metadata(path)
                rows.append(row)
                print(f"Processed {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    if not rows:
        print("No data found.")
        return

    df = pd.DataFrame(rows)
    # Convert types
    df["environment_size"] = pd.to_numeric(df["environment_size"], errors="coerce")
    df["dirt_rate"] = pd.to_numeric(df["dirt_rate"], errors="coerce")
    df["final_performance"] = pd.to_numeric(df["final_performance"], errors="coerce")

    dirt_rates = [0.1, 0.2, 0.4, 0.8]
    env_sizes = [2, 4, 8, 16, 32, 64, 128]

    for dirt_rate in dirt_rates:
        plt.figure(figsize=(12, 7))
        subset = df[df["dirt_rate"] == dirt_rate]
        if subset.empty:
            print(f"No data for dirt_rate {dirt_rate}")
            continue
        sns.boxplot(
            data=subset,
            x="environment_size",
            y="final_performance",
            hue="agent_type",
            order=env_sizes,
            showmeans=True,
            meanprops={
                "marker": "o",
                "markerfacecolor": "red",
                "markeredgecolor": "black",
            },
        )
        plt.title(
            f"Final Performance by Environment Size and Agent Type (Dirt Rate {dirt_rate})"
        )
        plt.xlabel("Environment Size")
        plt.ylabel("Final Performance")
        plt.legend(title="Agent Type")
        plt.tight_layout()
        plt.savefig(f"boxplot_dirt_rate_{str(dirt_rate).replace('.', '_')}.png")
        plt.close()


if __name__ == "__main__":
    main()
