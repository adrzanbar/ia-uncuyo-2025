"""
Search (Chapters 3-4)

The way to use this code is to subclass Problem to create a class of problems,
then create problem instances and solve them with calls to the various search
functions.
"""

import sys
import random
import numpy as np

from utils import is_in, probability, weighted_sampler


class Problem:
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value. Hill Climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError


# ______________________________________________________________________________


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [
            self.child_node(problem, action) for action in problem.actions(self.state)
        ]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action)
        next_node = Node(
            next_state,
            self,
            action,
            problem.path_cost(self.path_cost, self.state, action, next_state),
        )
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    # We want for a queue of nodes in breadth_first_graph_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        # We use the hash value of the state
        # stored in the node instead of the node
        # object itself to quickly search a node
        # with the same state in a Hash Table
        return hash(self.state)


# ______________________________________________________________________________
# Other search algorithms


def hill_climbing(problem):
    """
    [Figure 4.2]
    From the initial node, keep choosing the neighbor with highest value,
    stopping when no neighbor is better.
    """
    current = Node(problem.initial)
    current_value = problem.value(current.state)
    while True:
        neighbors = current.expand(problem)
        if not neighbors:
            break

        values = [problem.value(n.state) for n in neighbors]
        best = max(values)

        if problem.h_series is not None:
            problem.h_series.append(best)

        if best <= current_value:
            break

        current = neighbors[values.index(best)]
        current_value = best

    return current.state


def exp_schedule(k=20, lam=0.005, limit=100):
    """One possible schedule function for simulated annealing"""
    return lambda t: (k * np.exp(-lam * t) if t < limit else 0)


def simulated_annealing(problem, schedule=None):
    """[Figure 4.5] CAUTION: This differs from the pseudocode as it
    returns a state instead of a Node."""
    if not schedule:
        schedule = problem.schedule()

    current = Node(problem.initial)
    current_value = problem.value(current.state)
    neighbors = current.expand(problem)

    for t in range(sys.maxsize):
        if not neighbors:
            return current.state

        if problem.goal_test(current.state, current_value):
            return current.state

        T = schedule(t)
        if T == 0:
            return current.state

        next_choice = random.choice(neighbors)
        delta_e = problem.value(next_choice.state) - current_value

        if delta_e > 0 or probability(np.exp(delta_e / T)):
            current = next_choice
            current_value = problem.value(current.state)

            if problem.h_series is not None:
                problem.h_series.append(current_value)

            neighbors = current.expand(problem)


# ______________________________________________________________________________
# Genetic Algorithm


def genetic_algorithm(problem, elitism=False, lamarckian=False):
    """[Figure 4.8]"""
    population = problem.population()
    for _ in range(problem.ngen):
        fitnesses = [problem.value(p) for p in population]

        best_fit = max(fitnesses)
        fittest_individual = population[fitnesses.index(best_fit)]

        if problem.h_series is not None:
            problem.h_series.append(best_fit)

        if best_fit >= problem.f_thres:
            return fittest_individual

        sampler = weighted_sampler(population, fitnesses)

        new_population = []

        if elitism:
            new_population.append(fittest_individual)

        for _ in range(len(population) - len(new_population)):
            parents = sampler(2)

            child = problem.reproduce(*parents)

            if random.uniform(0, 1) < problem.pmut:
                child = problem.mutate(child)

            new_population.append(child)

        if lamarckian and problem.improve is not None:
            idx = random.randrange(len(new_population))
            improved = problem.improve(new_population[idx])
            new_population[idx] = improved

        population = new_population

    return max(population, key=problem.value)


def init_population(gene_pool, state_length, pop_number=20):
    """Initializes population for genetic algorithm
    pop_number  :  Number of individuals in population
    gene_pool   :  List of possible values for individuals
    state_length:  The length of each individual"""
    population = []
    for _ in range(pop_number):
        new_individual = tuple(random.sample(gene_pool, state_length))
        population.append(new_individual)

    return population


def recombine(x, y):
    n = len(x)
    c = random.randrange(0, n)
    return x[:c] + y[c:]


def mutate(x, gene_pool):
    n = len(x)
    g = len(gene_pool)
    c = random.randrange(0, n)
    r = random.randrange(0, g)

    new_gene = gene_pool[r]
    return tuple(list(x[:c]) + [new_gene] + list(x[c + 1 :]))


# ______________________________________________________________________________


class NQueensProblem(Problem):
    def __init__(self, N, seed=None, initial=None, ngen=sys.maxsize, pmut=0.2):
        if initial is not None:
            super().__init__(initial)
        else:
            rng = random.Random(seed)
            super().__init__(tuple(rng.sample(range(N), N)))

        self.N = N
        self.MAX_PAIRS = N * (N - 1) // 2

        # GA specific attributes
        self.gene_pool = tuple(range(N))
        self.state_length = N
        self.f_thres = self.MAX_PAIRS
        self.ngen = ngen
        self.pmut = pmut

    def actions(self, state):
        return [(i, j) for i in range(self.N) for j in range(i + 1, self.N)]

    def result(self, state, action):
        i, j = action
        state = list(state)
        state[i], state[j] = state[j], state[i]
        return tuple(state)

    def goal_test(self, state, cached_value=None):
        if cached_value is not None:
            return cached_value == self.MAX_PAIRS
        return self.value(state) == self.MAX_PAIRS

    def value(self, state):
        return self.MAX_PAIRS - self.num_conflicts(state)

    def num_conflicts(self, state):
        max_diagonal = 2 * self.N - 1
        main_diagonal = [0] * max_diagonal
        anti_diagonal = [0] * max_diagonal
        count = 0

        for col, row in enumerate(state):
            main_key = row - col + self.N - 1  # Shift index to be non-negative
            anti_key = row + col

            # Count conflicts in main diagonal
            count += main_diagonal[main_key]
            main_diagonal[main_key] += 1

            # Count conflicts in anti diagonal
            count += anti_diagonal[anti_key]
            anti_diagonal[anti_key] += 1

        return count

    # SA specific methods

    def schedule(self):
        return exp_schedule(k=self.N, lam=1 / self.N, limit=sys.maxsize)

    # GA specific methods

    def population(self):
        return init_population(self.gene_pool, self.state_length, self.N * self.N)

    def reproduce(self, x, y):
        """Order Crossover"""
        c1, c2 = sorted(random.sample(range(self.state_length), 2))

        child = [None] * self.state_length

        # copy slice from parent1
        child[c1:c2] = list(x[c1:c2])

        # mark taken genes
        taken = [False] * self.state_length
        for i in range(c1, c2):
            taken[child[i]] = True

        # fill remaining positions from parent2 in order
        fill_pos = c2 % self.state_length
        for gene in y:
            if not taken[gene]:
                child[fill_pos] = gene
                taken[gene] = True
                fill_pos = (fill_pos + 1) % self.state_length

        return tuple(child)

    def mutate(self, x, gene_pool=None):
        """Swap mutation. Preserves permutation property"""
        n = len(x)
        i, j = random.sample(range(n), 2)
        x_list = list(x)
        x_list[i], x_list[j] = x_list[j], x_list[i]
        return tuple(x_list)

    def improve(self, state):
        subproblem = InstrumentedProblem(NQueensProblem(self.N, initial=state))
        improved = hill_climbing(subproblem)
        return improved, subproblem.states, subproblem.h_series


# ______________________________________________________________________________

# Code to compare searchers on various problems.


class InstrumentedProblem(Problem):
    """Delegates to a problem, and keeps statistics."""

    def __init__(self, problem):
        self.problem = problem
        self.succs = self.goal_tests = self.states = 0
        self.found = None
        self.h_series = [self.problem.value(self.problem.initial)]

    def actions(self, state):
        self.succs += 1
        return self.problem.actions(state)

    def result(self, state, action):
        return self.problem.result(state, action)

    def goal_test(self, state, cached_value=None):
        self.goal_tests += 1
        result = self.problem.goal_test(state, cached_value)
        if result:
            self.found = state
        return result

    def path_cost(self, c, state1, action, state2):
        return self.problem.path_cost(c, state1, action, state2)

    def value(self, state):
        self.states += 1
        return self.problem.value(state)

    def __getattr__(self, attr):
        return getattr(self.problem, attr)

    def __repr__(self):
        return "<{:4d}/{:4d}/{:4d}/{}>".format(
            self.succs, self.goal_tests, self.states, str(self.found)[:4]
        )

    def improve(self, state):
        improved, states, h_series = self.problem.improve(state)
        self.states += states
        self.h_series.extend(h_series)
        return improved
