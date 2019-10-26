import wiktionaryReader
import mirriamReader
import argparse
from wordData import wordData
import logging

from pprint import pprint


def main():

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

    


if __name__ == "__main__":
    main()