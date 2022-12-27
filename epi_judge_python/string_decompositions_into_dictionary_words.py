from typing import List

from test_framework import generic_test

import collections
def find_all_substrings(s: str, words: List[str]) -> List[int]:
    # TODO - you fill in here.
    
    def match_all_words_in_dict(start_idx):
        curr_string_to_freq = collections.Counter()
        for i in range(start_idx, start_idx+len(words)*unit_size, unit_size):
            curr_word = s[i:i+unit_size]
            if word_to_freq[curr_word] == 0:
                return False
            curr_string_to_freq[curr_word]+=1
            if curr_string_to_freq[curr_word]>word_to_freq[curr_word]:
                ## curr_word occurs too frequently that we can't satisfy the need for it from words in the dictionary.
                return False
        return True
    
    word_to_freq = collections.Counter(words)
    
    unit_size = len(words[0])
    result = []
    for i in range(len(s)-unit_size*len(words)+1):
        if match_all_words_in_dict(i):
            result.append(i)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
