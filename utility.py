import random


class utility:

    @staticmethod
    def halve_word(word):
        word_length = len(word)

        if word_length % 2 > 0:
            midpoint = int((word_length + 1) / 2)
        else:
            midpoint = int(word_length / 2)

        word_splits = {
            "beginning": word[:midpoint],
            "endpoint": word[midpoint:]
        }

        return word_splits

    @staticmethod
    def create_letter_list(word):
        letter_list = []

        for letter in word:
            letter_list.append(letter)

        return letter_list

    @staticmethod
    def add_letters(word_dict, list):
        word_dict['random_index'] = random.randint(0, len(list) - 1)
        word_dict['word'] = word_dict['word'] + word_dict['random_index']
        list.pop(random_index)
