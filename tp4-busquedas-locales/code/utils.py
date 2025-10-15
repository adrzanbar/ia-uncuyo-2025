"""Provides some utilities widely used by other modules"""

import bisect
import random

# ______________________________________________________________________________
# Functions on Sequences and Iterables


def is_in(elt, seq):
    """Similar to (elt in seq), but compares with 'is', not '=='."""
    return any(x is elt for x in seq)


def shuffled(iterable):
    """Randomly shuffle a copy of iterable."""
    items = list(iterable)
    random.shuffle(items)
    return items


# ______________________________________________________________________________
# Statistical and mathematical functions


def probability(p):
    """Return true with probability p."""
    return p > random.uniform(0.0, 1.0)


def weighted_sampler(seq, weights):
    """Return a random-sample function that picks k elements from seq weighted by weights, without replacement."""
    totals = []
    for w in weights:
        totals.append(w + totals[-1] if totals else w)

    def sampler(k):
        temp_seq = list(seq)  # Create a temporary copy of seq
        temp_totals = list(totals)  # Create a temporary copy of totals
        result = []

        for _ in range(k):
            rand_val = random.uniform(0, temp_totals[-1])
            index = bisect.bisect_left(temp_totals, rand_val)
            result.append(temp_seq[index])

            # Remove selected element from temporary copies
            del temp_seq[index]
            del temp_totals[index]

            # Update temporary totals
            for i in range(index, len(temp_totals)):
                temp_totals[i] -= weights[index]

        return result

    return sampler
