import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    # TODO - you fill in here.
    endpoints = []
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))
    for event in A:
        e1 = Endpoint(event.start, True)
        e2 = Endpoint(event.finish, False)
        endpoints.append(e1)
        endpoints.append(e2)
    endpoints.sort(key= lambda x: (x.time,not x.is_start))
    count = 0
    ans = 0
    for e in endpoints:
        if e.is_start:
            count +=1
            ans = max(ans, count)
        else:
            count -=1
    return ans



@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
