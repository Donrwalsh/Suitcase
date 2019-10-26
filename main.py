import wiktionaryReader
import mirriamReader
import argparse
import logging


def main():

    # Argparse block - built to test functionality
    input_parser = argparse.ArgumentParser(description='For the purpose of testing distinct dictionary calls at CLI')
    input_parser.add_argument('word', type=str)
    input_parser.add_argument('-w', '--wiki', action='store_true', help='Turns on submitting word to wiki')
    input_parser.add_argument('-m', '--mirriam', action='store_true', help='Turns on submitting word to mirriam')


    args = input_parser.parse_args()

    if args.wiki and args.mirriam:
        # Lookup word in wiki and mirriam
        print(f'Look up {args.word} in wiki and mirriam')
    elif args.wiki:
        # Lookup word in wiki
        print(f'Look up {args.word} in wiki')
    else:
        # Lookup word in mirriam
        print(f'Look up {args.word} in mirriam')


if __name__ == "__main__":

    main()