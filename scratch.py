# Argparse block - built to test functionality
    input_parser = argparse.ArgumentParser(description='For the purpose of testing distinct dictionary calls at CLI')
    input_parser.add_argument('word', type=str)
    input_parser.add_argument('-w', '--wiki', action='store_true', help='Turns on submitting word to wiki')
    input_parser.add_argument('-m', '--mirriam', action='store_true', help='Turns on submitting word to mirriam')


    args = input_parser.parse_args()

    test_words = args.word.split(",")
    wiki = wiktionary_reader.wiktionaryReader()
    mirriam = mirriamReader.mirriamReader()

    if len(test_words) > 2:
        print("Sorry, this only accepts two words.")
        exit(1)

    word_data = []
    for word in test_words:
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

# Specific word combine method print statements

print(f'Halves Word Is: {halves.combine.words(word_one, word_two).word}')
print(f'Without Replacement Word Is: {without_replacement.combine.words(word_one, word_two).word}')
print(f'Without Replacement and Random Vowels Word Is: {without_replacement_random_vowels.combine.words(word_one,
                                                                                                        word_two).word}')

    print(f'{word_one}\n'
           f'{word_data[0].definition_list}')

    print(f'{word_two}\n'
           f'{word_data[1].definition_list}')

    test = combiner()
    print(f'Final Word Is: {test.combine_by_halves(word_one, word_two)}')
    print(f'Other Final Word Is: {test.combine_without_replacement(word_one, word_two)}')