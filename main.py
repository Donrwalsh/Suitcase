import objects.dictApi.wiktionaryReader
import mirriamReader
import argparse
from objects.combiners import *
from objects.wordData import wordData
import random


def main():

    test_words = ['gorilla', 'friend', "python", "jumble", "easy", "difficult", "answer",  "xylophone", "earsplitting",
             "utmost", "unsightly", "efficacious", "contagious", "amusement"]

    word_one = wordData(test_words[random.randint(0, len(test_words)-1)])
    word_two = wordData(test_words[random.randint(0, len(test_words)-1)])


    print(f'word_one: {word_one.word},  word_two: {word_two.word}')
    print(f'Halves Word Is: {halves.combine.words(word_one, word_two).word}')
    print(f'Without Replacement Word Is: {without_replacement.combine.words(word_one, word_two).word}')

    exit(0)


if __name__ == "__main__":
    main()