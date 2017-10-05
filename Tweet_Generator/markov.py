from pprint import pprint
from Tweet_Generator import tokenize, sample
from Tweet_Generator.histograms import Dictogram
from collections import ChainMap

fh = tokenize.tokenize('./../SoP.txt')


def markov_chain(words_list):
    word_dict = Dictogram()
    generated_histogram = Dictogram()
    for x in range(len(words_list)):
        current_word = words_list[x]

        if x + 1 < len(words_list):
            next_word = words_list[x + 1]
            generated_histogram.add(next_word)
            if current_word in word_dict:
                word_dict[current_word] = dict(ChainMap(word_dict[current_word], {next_word: generated_histogram[next_word]}))
            else:
                word_dict[current_word] = {next_word: generated_histogram[next_word]}
    return word_dict


def weighted_markov(markov_dict):
    # dictionize = dict(markov_dict)
    pprint(markov_dict.tokens)

    for markov in markov_dict:
        histogram = markov_dict[markov]
        weighted_dicts = sample.create_weighted_sorted_tuple_list_markov(histogram)
        markov_dict[markov] = weighted_dicts

    pprint(markov_dict)

markov_chain_var = markov_chain(fh)
weighted_markov(markov_chain_var)
# pprint(markov_chain_var)