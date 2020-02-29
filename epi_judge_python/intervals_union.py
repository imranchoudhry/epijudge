import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):
    # TODO - you fill in here.
    def is_overlap(interval1, interval2):
        if interval2.left.val < interval1.right.val or \
        interval2.left.val <= interval1.right.val and (interval2.left.is_closed or interval1.right.is_closed) or \
        interval1.left.val < interval2.right.val < interval1.right.val or \
        interval2.right.val <= interval1.right.val and (interval2.right.is_closed or interval1.right.is_closed):
            return True
        else:
            return False


        #return e1.left.val  <= e2.left.val <= e1.right.val or e1.left.val <= e2.right.val <= e1.right.val


    intervals.sort(key=lambda i: (i.left[1], not i.left.is_closed))

    #print(intervals)
    ret = [intervals[0]]

    for interval in intervals:
        prev = ret[-1]
        if is_overlap(prev, interval):
            if interval.right.val > prev.right.val:
                ret[-1] = Interval(prev.left, interval.right)
            elif interval.right.val == prev.right.val and (interval.right.is_closed or prev.right.is_closed):
                ret[-1] = Interval(prev.left, Endpoint(True, interval.right.val))
            else:
                ret[-1] = Interval(prev.left, prev.right)
        else:
            ret.append(interval)
    
    return ret


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
