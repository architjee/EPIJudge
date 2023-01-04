import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    # TODO - you fill in here.
    s.reverse()
    def reverse_range(s, start, end):
        while start< end:
            s[start], s[end] = s[end], s[start]
            start+=1
            end -=1
    def custom_find(s, start, search_ele):
        for x in range(start, len(s)):
            if s[x] == search_ele:
                return x
        return -1
    start = 0
    while True:
        end = custom_find(s, start, ' ')
        if end<0:
            break
        reverse_range(s, start, end-1)
        start = end + 1
    reverse_range(s, start, len(s)-1)



@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
