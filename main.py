import objects.dictApi.wiktionaryReader
import mirriamReader
import argparse
from objects.wordData import wordData
from combiner import combiner
import random


def main():

    test_words = ['gorilla', 'friend', "python", "jumble", "easy", "difficult", "answer",  "xylophone", "earsplitting",
             "utmost", "unsightly", "efficacious", "contagious", "amusement"]

    word_one = wordData(test_words[random.randint(0, len(test_words)-1)])
    word_two = wordData(test_words[random.randint(0, len(test_words)-1)])


    test = combiner()

    print(f'word_one: {word_one.word},  word_two: {word_two.word}')
    halves = test.combine_words(word_one, word_two)
    print(f'Final Word Is: {halves.word}')
    mix = test.combine_words_two(word_one, word_two)
    print(f'Other Final Word Is: {mix.word}')

    exit(0)

if __name__ == "__main__":
    main()