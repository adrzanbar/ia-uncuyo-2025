# TP6 — Q-Learning Agent

This TP trains and evaluates a Q-learning attacker agent against the NetSecGame environment.

## What's in this folder

- `q_agent.py` — the Q-learning agent implementation (the course template with the three TODOs implemented: `max_action_q`, epsilon-greedy `select_action`, and the Q-learning update in `play_game`).
- (Cloned repos below are intentionally **not** committed here — get them with the exact commits listed.)

## Pinned repositories and commits

| Repo | URL | Commit |
|---|---|---|
| NetSecGame (game server) | https://github.com/stratosphereips/NetSecGame | `2ee09f2ac967e7d1256b524675e5ecab494157e5` (2025-10-01) |
| NetSecGameAgents-AI-Course (agents, fork) | https://github.com/harpomaxx/NetSecGameAgents-AI-Course | `36bcb30b90c2f871dce8859b8b8e741edb553628` (2025-10-06) |

> Note: the commit of the agents repo does **not** include the Q-learning implementation; it is the template. Use the `q_agent.py` in this folder.

## Requirements

- Linux or WSL
- [uv](https://docs.astral.sh/uv/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- Python 3.12 (installed automatically by `uv venv --python 3.12` if missing)

## Setup

```bash
# 1. Clone the game server at the pinned commit
git clone https://github.com/stratosphereips/NetSecGame
cd NetSecGame
git checkout 2ee09f2ac967e7d1256b524675e5ecab494157e5
cd ..

# 2. Clone the agents at the pinned commit.
#    The folder name MUST be "NetSecGameAgents" — the editable install and imports depend on it.
git clone https://github.com/harpomaxx/NetSecGameAgents-AI-Course NetSecGameAgents
cd NetSecGameAgents
git checkout 36bcb30b90c2f871dce8859b8b8e741edb553628
cd ..
```

The implementation lives in `q_agent.py` (this folder), **not** in the fork — the fork stays pristine.

## Run the server (terminal 1)

```bash
cd NetSecGame
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e .
python -m AIDojoCoordinator.worlds.NSEGameCoordinator \
  --task_config=./examples/example_task_configuration.yaml \
  --game_port=9000
```

## Run the agent (terminal 2)

Recommended: separate venv for the agent.

Copy the implementation into the fork (keeps the fork pristine — revert with `git checkout` after):

```bash
cp q_agent.py NetSecGameAgents/agents/attackers/q_learning/q_agent.py
```

```bash
cd NetSecGameAgents
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e ".[q_learning]"
cd ..
WANDB_MODE=offline python -m NetSecGameAgents.agents.attackers.q_learning.q_agent
```

Restore the fork to pristine anytime: `git -C NetSecGameAgents checkout -- agents/attackers/q_learning/q_agent.py`

`WANDB_MODE=offline` is required unless you have `wandb login` configured on the machine;
without credentials the agent hangs at the wandb login prompt. Metrics are stored locally
in `./wandb/` in this mode — do not commit that folder.

## Default parameters

No flags = defaults: `--episodes 15000`, `--alpha 0.1`, `--gamma 0.9`,
`--epsilon_start 0.9`, `--epsilon_end 0.1`, `--epsilon_max_episodes 8000`.

Quick smoke test: add `--episodes 1`.
Real training: leave the defaults, or e.g. `--episodes 15000 --alpha 0.1 --gamma 0.9`.
`--early_stop_threshold` (default 95) stops training when the test win rate exceeds it.

## Checking results

- Logs: `<agents>/agents/attackers/q_learning/logs/q_agent.log`
- Saved Q-table: `q_agent_marl.experiment.pickle` in the directory the agent was run from (see `--store_models_every`).
