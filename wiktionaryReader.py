import dictionaryApiBaseClass
from wiktionaryparser import WiktionaryParser
import random

class wiktionaryReader(dictionaryApiBaseClass.dictionaryAPIBaseClass):

    def __init__(self):
        self.parser = WiktionaryParser()

    def __del__(self):
        pass

    def word_definition(self, word):
        retrieved_definitions = self.parser.fetch(word)
        definition_list = retrieved_definitions[0]['definitions'][0]['text']
        definition=definition_list[random.randrange(1, len(definition_list))]
        return definition

