from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    # TODO - you fill in here.
    dp_array = [ [1]+[0]*final_score 
        for _ in individual_play_scores]
    for i in range(len(individual_play_scores)):
        for j in range(1, final_score+1):
            without_this_num = (dp_array[i-1][j] if i>=1 else 0)
            with_this_num = (dp_array[i][j-individual_play_scores[i]] if j>=individual_play_scores[i] else 0)
            dp_array[i][j] = without_this_num + with_this_num
    # print(dp_array)
    return dp_array[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
