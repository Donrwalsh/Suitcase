from objects.dictApi import *
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

    word_combiners = [word_halves, word_without_replacement, word_without_replacement_random_vowels]

    random_word_combiner = random.choice(word_combiners)
    print(f'word_one: {word_one.word} |  word_two: {word_two.word}')
    print(f'Combined Word is: {random_word_combiner.combine.words(word_one, word_two).word}')

    wiki = wiktionary.wiktionary()
    word_one.set_definition_list(wiki.word_definition(word_one.word))
    word_two.set_definition_list(wiki.word_definition(word_two.word))

    print(f'Word One Definition: {word_one.definition}\n'
          f'Word Two Definition: {word_two.definition}')



if __name__ == "__main__":
    main()