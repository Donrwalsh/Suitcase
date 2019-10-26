import objects.dictApi.wiktionaryReader
import mirriamReader
import argparse
from objects.combiners import *
from objects.wordData import wordData
import random


def main():

    test_words = ['gorilla', 'friend', 'python', 'jumble', 'easy', 'difficult', 'answer',  'xylophone', 'earsplitting',
             'utmost', 'unsightly', 'efficacious', 'contagious', 'amusement', 'and', 'pants', 'the', 'a', 'i']

    word_one = wordData(test_words[random.randint(0, len(test_words)-1)])
    word_two = wordData(test_words[random.randint(0, len(test_words)-1)])

    word_combiners = [halves, without_replacement, without_replacement_random_vowels]

    random_word_combiner = random.choice(word_combiners)
    print(f'Combiner is {str(random_word_combiner)}')
    print(f'word_one: {word_one.word} |  word_two: {word_two.word}')
    print(f'Combined Word is: {random_word_combiner.combine.words(word_one, word_two).word}')


if __name__ == "__main__":
    main()