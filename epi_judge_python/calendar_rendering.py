import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):
    # TODO - you fill in here.
    def is_overlap(e1, e2):
        return e1.start <= e2.start <= e1.finish or e1.start <= e2.finish <= e1.finish

    if not A:
        return 0

    endpoint_array = []
    for event in A:
        start = (event.start, 0)
        end = (event.finish, 1)
        endpoint_array.append(start)
        endpoint_array.append(end)

    #A.sort(key=lambda event: event.start)
    endpoint_array.sort()

    counter = 0
    max_counter = 0
    for endpoint in endpoint_array:
        if endpoint[1]== 0:
            counter += 1
        elif endpoint[1]==1:
            counter -= 1
        max_counter = max(max_counter, counter)

    return max_counter

    """

    max_overlaps = 1

    for i in range(1,len(A)):
        current_event = A[i]
        current_event_overlap = 1
        for j in range(0,i):
            if is_overlap(A[j], current_event):
                current_event_overlap += 1
        max_overlaps = max(max_overlaps, current_event_overlap)


    return max_overlaps
    """


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
