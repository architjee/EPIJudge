from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    import bisect
    result =  bisect.bisect_left(A,k)
    if result>len(A)-1:
        return -1
    elif A[result]==k:
        return result
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
