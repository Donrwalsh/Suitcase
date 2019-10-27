from .baseDictApi import dictionaryAPIBaseClass
from wiktionaryparser import WiktionaryParser
import random


class wiktionary(dictionaryAPIBaseClass):

    def __init__(self):
        self.parser = WiktionaryParser()

    def __del__(self):
        pass

    def word_definition(self, word):
        try:
            retrieved_definitions = self.parser.fetch(word)
        except Exception as e:
            print(f'An exception was raised when calling wiki API: {e}')
            exit(1)

        definition_list = retrieved_definitions[0]['definitions'][0]['text']
        definition = definition_list[random.randrange(1, len(definition_list))]
        return definition

    def word_check(self, word):

        if not self.parser.fetch(word)[0]['definitions']:
            return False
        else:
            return True

