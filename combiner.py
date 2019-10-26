import random
from utility import utility
from objects.


class combiner:

    def __init__(self):
        pass

    def combine_words(self, word_one, word_two):

        beginnings = [utility.halve_word(word_one)['beginning'], utility.halve_word(word_two)['beginning']]
        ends = [utility.halve_word(word_one)['endpoint'], utility.halve_word(word_two)['endpoint']]

        beginning_value = random.randint(0,1)
        ending_value = random.randint(0,1)
        final_word = (beginnings[beginning_value] + ends[ending_value])

        return final_word

    def combine_words_two(self, word_one, word_two):

        letter_list_one = utility.create_letter_list(word_one)
        letter_list_two = utility.create_letter_list(word_two)



        new_word = {
             'word':'',
             'word_length':0,
             'max_length':len(letter_list_one) + len(letter_list_two),
             'random_index':0
             }

        while new_word > 1:
            selector = random.randint(0, 1)
            if selector == 0:
                utility.add_letters(new_word, letter_list_one)
            else:
                utility.add_letters(new_word, letter_list_two)
                random_index = random.randint(0, len(letter_list_two)-1)
                new_word = new_word + letter_list_two[random_index]
                letter_list_two.pop(random_index)
            new_word['max_length'] -= random.randint(1, int(max_length/2))
            new_word['new_word_length'] += 1
        return new_word