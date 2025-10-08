import os
import json
import csv

DATA_DIR = "../game_data"
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


def extract_json_to_csv(
    data_dir=DATA_DIR, output_csv="simple-reflex-agent-experiment-128-8.csv"
):
    files = [f for f in os.listdir(data_dir)]
    rows = []
    for file in files:
        with open(os.path.join(data_dir, file), "r") as f:
            data = json.load(f)
            meta = data.get("metadata", {})
            row = [meta.get(col, "") for col in HEADER]
            rows.append(row)
    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(HEADER)
        writer.writerows(rows)


if __name__ == "__main__":
    extract_json_to_csv()
