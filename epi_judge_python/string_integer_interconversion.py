from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    is_negative = False
    if x<0:
        is_negative, x = True, -x
    s = []
    while True:
        s.append(chr(ord('0')+x%10))
        x//=10
        if x==0:
            break
    return  ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    is_negative = False
    
    partial_sum = 0
    for index, char in enumerate(s):
        if char=='+' and index==0:
            is_negative = False
            continue
        if char=='-' and index==0:
            is_negative = True
            continue
        partial_sum *= 10
        partial_sum += ord(char) - ord('0')
    if is_negative:
        return -partial_sum 
    return partial_sum


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
