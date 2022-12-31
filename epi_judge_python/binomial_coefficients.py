from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    # TODO - you fill in here.
    d={}
    def aux_binomial_coefficient(x, y):
        ## The function is x choose y.
        if y==0 or y==x:
            return 1
        key = (x, y)
        if key not in d:
            d[key] = aux_binomial_coefficient(x-1, y)+aux_binomial_coefficient(x-1, y-1)
        return d[key]
    return aux_binomial_coefficient(n, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
