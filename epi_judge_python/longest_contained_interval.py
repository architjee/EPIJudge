from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    unprocessed_entries = set(A)
    max_interval_size = 0
    while unprocessed_entries:
        a = unprocessed_entries.pop()

        ## Find the lower bound of the largest range containing a
        lower = a-1
        while lower in unprocessed_entries:
            unprocessed_entries.remove(lower)
            lower -= 1
        upper = a+1
        while upper in unprocessed_entries:
            unprocessed_entries.remove(upper)
            upper +=1
        max_interval_size= max(max_interval_size, upper-lower-1)
    return max_interval_size


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
