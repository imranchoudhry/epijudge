import functools
import random
from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def random_subset(n, k):
    # TODO - you fill in here.
    result = set()

    while len(result) < k:
        r = random.randint(0, n-1)

        result.add(r)
    return list(result)


def random_subset2(n, k):
    # TODO - you fill in here.

    d = {}
    for i in range(k):
        r = random.randint(i, n-1)
        elt_at_r = d.get(r,r)
        elt_at_i = d.get(i,i)
        d[r] = elt_at_i
        d[i] = elt_at_r
    l = []
    for i in range(k):
        l.append(d[i])
    return l


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0)
             for result in results], total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("random_subset.py", 'random_subset.tsv',
                                       random_subset_wrapper))
