from .combiner import combiner
from .utility import *
import random
from objects.wordData import wordData


class combine(combiner):

    @staticmethod
    def words(word_one, word_two):
        letter_list_one = utility.create_letter_list(word_one)
        letter_list_two = utility.create_letter_list(word_two)
        final_word = wordData('')

        if len(letter_list_one) == 1 or len(letter_list_two) == 1:
            print('That\'s not very fun, try again!')
            exit(0)

        popped_letter = ''

        max_length = len(letter_list_one) + len(letter_list_two)

        while max_length > 1:
            selector = random.randint(0, 1)
            if selector == 0 and len(letter_list_one) > 1:
                random_index = random.randint(0, len(letter_list_one)-1)
                if utility.is_vowel(letter_list_one[random_index]) and utility.is_vowel(popped_letter):
                    continue
                else:
                    final_word.word = final_word.word + letter_list_one[random_index]
                popped_letter = letter_list_one.pop(random_index)
            elif selector == 1 and len(letter_list_two) > 1:
                random_index = random.randint(0, len(letter_list_two)-1)
                if utility.is_vowel(letter_list_two[random_index]) and utility.is_vowel(popped_letter):
                    continue
                else:
                    final_word.word = final_word.word + letter_list_two[random_index]
                popped_letter = letter_list_two.pop(random_index)
            max_length -= random.randint(1, int(max_length/2))

        return final_word