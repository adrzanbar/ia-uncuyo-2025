import random
import time
import csv
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
from search import (
    Problem,
    InstrumentedProblem,
    Node,
    breadth_first_graph_search,
    depth_first_graph_search,
    uniform_cost_search,
    astar_search,
)


class FrozenLakeProblem(Problem):
    def __init__(self, size=100, p=0.92, seed=0):
        super().__init__(0, size * size - 1)
        self.desc = generate_random_map(size, p, seed)

    def actions(self, state):
        if state == self.goal:
            return []

        row, col = divmod(state, len(self.desc))

        if self.desc[row][col] == "H":
            return []

        actions = []
        if col > 0 and self.desc[row][col - 1] != "H":
            actions.append(0)  # left
        if row < len(self.desc) - 1 and self.desc[row + 1][col] != "H":
            actions.append(1)  # down
        if col < len(self.desc[row]) - 1 and self.desc[row][col + 1] != "H":
            actions.append(2)  # right
        if row > 0 and self.desc[row - 1][col] != "H":
            actions.append(3)  # up

        return actions

    def result(self, state, action):
        if action == 0:  # left
            state -= 1
        elif action == 1:  # down
            state += len(self.desc)
        elif action == 2:  # right
            state += 1
        elif action == 3:  # up
            state -= len(self.desc)

        return state

    def goal_test(self, state):
        return state == self.goal


class UniformCostFrozenLakeProblem(FrozenLakeProblem):
    def __name__():
        return "UniformCostFrozenLakeProblem"

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def h(self, node):
        row1, col1 = divmod(node.state, len(self.desc))
        row2, col2 = divmod(self.goal, len(self.desc))
        return abs(row1 - row2) + abs(col1 - col2)


class VerticalCostFrozenLakeProblem(FrozenLakeProblem):
    def __name__():
        return "VerticalCostFrozenLakeProblem"

    def path_cost(self, c, state1, action, state2):
        if action == 1 or action == 3:  # down or up
            return c + 10
        else:  # left or right
            return c + 1

    def h(self, node):
        row1, col1 = divmod(node.state, len(self.desc))
        row2, col2 = divmod(self.goal, len(self.desc))
        return abs(row1 - row2) * 10 + abs(col1 - col2)


def random_search(problem):
    current_node = Node(problem.initial)
    while not problem.goal_test(current_node.state):
        actions = problem.actions(current_node.state)
        if not actions:
            return None
        action = random.choice(actions)
        current_node = current_node.child_node(problem, action)

    return current_node


def run_experiment(algorithm, problem_class, size=100, p=0.92, n_runs=30, **kwargs):
    print()
    print(f"Running {algorithm.__name__} on {problem_class.__name__}")
    print(f"Parameters: size={size}, p={p}, n_runs={n_runs}, kwargs={kwargs}")
    results = []

    for seed in range(n_runs):
        problem = problem_class(size=size, p=p, seed=seed)

        print()
        print(f"Run with seed {seed} of {n_runs}")
        print(f"Environment:\n{problem.desc}")

        instrumented_problem = InstrumentedProblem(problem)
        start_time = time.time()

        result = algorithm(instrumented_problem, **kwargs)

        end_time = time.time()

        execution_time = end_time - start_time

        print()
        print("Path:\n", [node.state for node in result.path()])

        if result is not None:
            results.append(
                {
                    "states": instrumented_problem.goal_tests,
                    "actions": len(result.solution()),
                    "cost": result.path_cost,
                    "time": execution_time,
                    "found": True,
                }
            )

        else:
            results.append(
                {
                    "states": instrumented_problem.goal_tests,
                    "actions": 0,
                    "cost": 0,
                    "time": execution_time,
                    "found": False,
                }
            )

    return results


def save_results_to_csv(data, filename="frozen_lake_results.csv"):
    """Save experiment results to a CSV file with flattened structure."""
    with open(filename, "w", newline="") as csvfile:
        fieldnames = [
            "environment",
            "algorithm",
            "run_number",
            "states",
            "actions",
            "cost",
            "time",
            "found",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for environment, algorithms in data.items():
            for algorithm, results in algorithms.items():
                for run_number, result in enumerate(results, 1):
                    row = {
                        "environment": environment,
                        "algorithm": algorithm,
                        "run_number": run_number,
                        **result,
                    }
                    writer.writerow(row)


if __name__ == "__main__":
    data = {
        "uniform_cost": {
            "random": run_experiment(random_search, UniformCostFrozenLakeProblem),
            "breadth_first": run_experiment(
                breadth_first_graph_search, UniformCostFrozenLakeProblem
            ),
            "depth_first": run_experiment(
                depth_first_graph_search, UniformCostFrozenLakeProblem
            ),
            "uniform_cost": run_experiment(
                uniform_cost_search, UniformCostFrozenLakeProblem
            ),
            "astar": run_experiment(astar_search, UniformCostFrozenLakeProblem),
        },
        "vertical_cost": {
            "random": run_experiment(random_search, VerticalCostFrozenLakeProblem),
            "breadth_first": run_experiment(
                breadth_first_graph_search, VerticalCostFrozenLakeProblem
            ),
            "depth_first": run_experiment(
                depth_first_graph_search, VerticalCostFrozenLakeProblem
            ),
            "uniform_cost": run_experiment(
                uniform_cost_search, VerticalCostFrozenLakeProblem
            ),
            "astar": run_experiment(astar_search, VerticalCostFrozenLakeProblem),
        },
    }

    save_results_to_csv(data)
