from .combiner import combiner
import utility
import random
from objects.wordData import wordData

class halves(combiner):

    @staticmethod
    def combine_words(word_one, word_two):
        letter_list_one = utility.create_letter_list(word_one)
        letter_list_two = utility.create_letter_list(word_two)
        final_word = wordData('')

        max_length = len(letter_list_one) + len(letter_list_two)

        while max_length > 1:
            selector = random.randint(0, 1)
            if selector == 0 and len(letter_list_one) > 0:
                random_index = random.randint(0, len(letter_list_one)-1)
                final_word.word = final_word.word + letter_list_one[random_index]
                letter_list_one.pop(random_index)
            elif selector == 1 and len(letter_list_two) > 0:
                random_index = random.randint(0, len(letter_list_two)-1)
                final_word.word = final_word.word + letter_list_two[random_index]
                letter_list_two.pop(random_index)
            else:
                print('Something went wrong with this.')
            max_length -= random.randint(1, int(max_length/2))

        return final_word