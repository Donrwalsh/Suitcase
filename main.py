from objects.dictApi import *
from objects.combiners import *
from objects.wordData import wordData
import random


def main():


    test_words = ['notaword', 'gorilla', 'friend', 'python', 'jumble', 'easy', 'difficult', 'answer',  'xylophone', 'earsplitting',
             'utmost', 'unsightly', 'efficacious', 'contagious', 'amusement', 'and', 'pants', 'the', 'a', 'i']


    word_one = wordData(test_words[random.randint(0, len(test_words)-1)])
    word_two = wordData(test_words[random.randint(0, len(test_words)-1)])

    word_combiners = [word_halves, word_without_replacement, word_without_replacement_random_vowels]

    random_word_combiner = random.choice(word_combiners)
    final_word = random_word_combiner.combine.words(word_one, word_two)

    print(f'word_one: {word_one.word} |  word_two: {word_two.word}')
    print(f'Combined Word is: {final_word.word}')

    wiki = wiktionary.wiktionary()
    if wiki.word_check(word_one.word) and wiki.word_check(word_two.word):
        word_one.set_definition_list(wiki.word_definition(word_one.word))
        word_two.set_definition_list(wiki.word_definition(word_two.word))
    else:
        print(f'I can only find definitions for real words, sorry!')
        exit(0)

    print(f'Word One Definition: {word_one.definition}\n'
          f'Word Two Definition: {word_two.definition}')

    definition_combiners = [definition_without_replacement]

    random_defintion_combiner = random.choice(definition_combiners)
    print(f'Combined Definition is: '
          f'    {random_defintion_combiner.combine.definitions(word_one, word_two, final_word).definition}')



if __name__ == "__main__":
    main()