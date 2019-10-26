import wiktionaryReader
import mirriamReader
import argparse
from objects.wordData import wordData
from combiner import combiner
import random


def main():

    words = ['gorilla', 'friend', "python", "jumble", "easy", "difficult", "answer",  "xylophone", "earsplitting",
             "utmost", "unsightly", "efficacious", "contagious", "amusement"]

    word_one = words[random.randint(0, len(words)-1)]
    word_two = words[random.randint(0, len(words)-1)]


    test = combiner()
    print(f'word_one: {word_one},  word_two: {word_two}')
    print(f'Final Word Is: {test.combine_words(word_one, word_two)}')
    print(f'Other Final Word Is: {test.combine_words_two(word_one, word_two)}')

    # Argparse block - built to test functionality
    input_parser = argparse.ArgumentParser(description='For the purpose of testing distinct dictionary calls at CLI')
    input_parser.add_argument('word', type=str)
    input_parser.add_argument('-w', '--wiki', action='store_true', help='Turns on submitting word to wiki')
    input_parser.add_argument('-m', '--mirriam', action='store_true', help='Turns on submitting word to mirriam')


    args = input_parser.parse_args()

    words = args.word.split(",")
    wiki = wiktionaryReader.wiktionaryReader()
    mirriam = mirriamReader.mirriamReader()

    if len(words) > 2:
        print("Sorry, this only accepts two words.")
        exit(1)

    word_data = []
    for word in words:
        new_word = wordData(word)
        if args.wiki and args.mirriam:
            # Lookup word in wiki and mirriam
            new_word.set_definition_list(wiki.word_definition((word)))
        elif args.wiki:
            # Lookup word in wiki
            new_word.set_definition_list(wiki.word_definition((word)))
        else:
            # Lookup word in mirriam
            print(f'Look up {new_word.word} in mirriam')
        word_data.append(new_word)

    word_one = word_data[0].word
    word_two = word_data[1].word

    print(f'{word_one}\n'
           f'{word_data[0].definition_list}')

    print(f'{word_two}\n'
           f'{word_data[1].definition_list}')

    test = combiner()
    print(f'Final Word Is: {test.combine_words(word_one, word_two)}')
    print(f'Other Final Word Is: {test.combine_words_two(word_one, word_two)}')

if __name__ == "__main__":
    main()