import random
from utility import utility

class combiner:

    def __init__(self):
        pass

    def combine_words(self, word_one, word_two, final_word):

        beginnings = [utility.halve_word(word_one.word)['beginning'], utility.halve_word(word_two.word)['beginning']]
        ends = [utility.halve_word(word_two.word)['endpoint'], utility.halve_word(word_two.word)['endpoint']]

        beginning_value = random.randint(0,1)
        ending_value = random.randint(0,1)
        final_word.word = (beginnings[beginning_value] + ends[ending_value])

        return final_word

    def combine_words_two(self, word_one, word_two, final_word):

        letter_list_one = utility.create_letter_list(word_one)
        letter_list_two = utility.create_letter_list(word_two)

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