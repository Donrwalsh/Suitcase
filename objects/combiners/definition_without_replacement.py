from .combiner import combiner
import random
import objects.wordData


class combine(combiner):

    @staticmethod
    def definitions(word_one, word_two, final_word):
        word_list_one = word_one.definition.split()
        word_list_two = word_two.definition.split()

        definition_length = len(word_list_one) + len(word_list_two) / 2

        while definition_length > 0:
            selector = random.randint(0,1)
            if selector == 0 and len(word_list_one) < 1:
                continue
            elif selector == 1 and len(word_list_two) < 1:
                continue
            elif selector == 0:
                random_index = random.randint(0, len(word_list_one) - 1)
                random.randint(0, len(word_list_one)-1)
                final_word.definition = final_word.definition + word_list_one[random_index].rstrip(".")  + " "
                word_list_one.pop(random_index)
            else:
                random_index = random.randint(0, len(word_list_two) - 1)
                random.randint(0, len(word_list_two)-1)
                final_word.definition = final_word.definition + word_list_two[random_index].rstrip(".") + " "
                word_list_two.pop(random_index)
            definition_length -= 1

        return final_word

