import argparse
import os
import ast
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def safe_eval_env_size(x):
    # environment_size column may contain a string representation of a tuple/list
    try:
        v = ast.literal_eval(x) if isinstance(x, str) else x
        # assume first element is width/size
        return v[0]
    except Exception:
        return x


def load_and_prepare(csv_path):
    df = pd.read_csv(csv_path)
    if "environment_size" in df.columns:
        df["env_size"] = df["environment_size"].apply(safe_eval_env_size)
    else:
        df["env_size"] = None
    return df


def grouped_boxplots(csv_files, dirt_rates, out_prefix="boxplot", agent_names=None):
    # Load all dataframes and associate label (agent name from filename)
    agents = []
    use_names = None
    if agent_names and len(agent_names) == len(csv_files):
        use_names = agent_names

    for idx, path in enumerate(csv_files):
        if not os.path.exists(path):
            print(f"Warning: CSV file not found: {path}. Skipping.")
            continue
        if use_names:
            label = use_names[idx]
        else:
            label = os.path.splitext(os.path.basename(path))[0]
        df = load_and_prepare(path)
        agents.append((label, df))

    if not agents:
        print("No CSV files loaded. Exiting.")
        return

    for dirt_rate in dirt_rates:
        # collect union of environment sizes across agents for this dirt rate
        env_size_set = set()
        agent_data_by_env = {}
        for label, df in agents:
            df_rate = df[df["dirt_rate"] == dirt_rate]
            env_sizes = sorted(df_rate["env_size"].dropna().unique())
            env_size_set.update(env_sizes)
            agent_data_by_env[label] = {
                size: df_rate[df_rate["env_size"] == size]["final_performance"].values
                for size in env_sizes
            }

        if not env_size_set:
            print(f"No data found for dirt rate {dirt_rate}. Skipping figure.")
            continue

        env_sizes = sorted(env_size_set)

        # Prepare data matrix: for each env size, create list of arrays (one per agent)
        # We'll arrange boxplots grouped per env size, with one box per agent in each group.
        data_groups = []  # flat list of arrays for plt.boxplot
        positions = []
        xticks = []
        labels_for_legend = [label for label, _ in agents]

        num_agents = len(agents)
        width = 0.6  # total width for group
        box_width = width / num_agents

        # Positions: for env i, center at i, agent j offset
        for i, env in enumerate(env_sizes, start=1):
            base = i
            for j, (label, _) in enumerate(agents):
                arr = agent_data_by_env.get(label, {}).get(env, [])
                data_groups.append(arr)
                # spread boxes around the integer tick
                offset = (j - (num_agents - 1) / 2) * box_width
                positions.append(base + offset)
            xticks.append((i, env))

        fig, ax = plt.subplots(figsize=(max(6, len(env_sizes) * 1.5), 6))

        bp = ax.boxplot(
            data_groups, positions=positions, widths=box_width * 0.9, patch_artist=True
        )

        # color each agent differently
        colors = plt.cm.tab10.colors
        for patch_idx, patch in enumerate(bp["boxes"]):
            agent_idx = patch_idx % num_agents
            patch.set_facecolor(colors[agent_idx % len(colors)])

        # set x ticks at integer positions
        ax.set_xticks([p[0] for p in xticks])
        # show only the environment size as the x-tick label (user requested no sample counts)
        ax.set_xticklabels([f"{env}" for _, env in xticks])

        ax.set_title(f"Agents comparison. Dirt Rate = {dirt_rate}")
        ax.set_xlabel("Environment Size")
        ax.set_ylabel("Final Performance")
        ax.grid(True)
        ax.set_ylim(bottom=0)

        # Create legend handles
        handles = [
            matplotlib.patches.Patch(
                color=colors[i % len(colors)], label=labels_for_legend[i]
            )
            for i in range(num_agents)
        ]
        ax.legend(handles=handles, loc="best")

        plt.subplots_adjust(bottom=0.2)
        out_file = f"{out_prefix}-{dirt_rate}.png"
        fig.savefig(out_file)
        plt.close(fig)
        print(f"Saved {out_file}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create grouped boxplots for multiple agents across dirt rates."
    )
    parser.add_argument(
        "csv_files", nargs="+", help="CSV files for agents (one per agent)"
    )
    parser.add_argument(
        "--dirt-rates",
        nargs="+",
        type=float,
        default=[0.1, 0.2, 0.4, 0.8],
        help="Dirt rates to create figures for",
    )
    parser.add_argument("--out-prefix", default="boxplot", help="Output file prefix")
    parser.add_argument(
        "--agent-names",
        nargs="+",
        help="Optional names for each agent CSV (must match number of csv_files)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    grouped_boxplots(args.csv_files, args.dirt_rates, args.out_prefix, args.agent_names)
