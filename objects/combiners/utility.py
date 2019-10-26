from .letter_attributes import *

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

        for letter in word.word:
            letter_list.append(letter)

        return letter_list

    @staticmethod
    def is_vowel(letter):
        if letter in vowels:
            return True
        else:
            return False




