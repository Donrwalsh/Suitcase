from .combiner import combiner
from .utility import *
import random
from objects.wordData import wordData

class combine(combiner):

    @staticmethod
    def words(word_one, word_two):
        beginnings = [utility.halve_word(word_one.word)['beginning'], utility.halve_word(word_two.word)['beginning']]
        ends = [utility.halve_word(word_two.word)['endpoint'], utility.halve_word(word_two.word)['endpoint']]

        beginning_value = random.randint(0,1)
        ending_value = random.randint(0,1)
        final_word = wordData(beginnings[beginning_value] + ends[ending_value])

        return final_word