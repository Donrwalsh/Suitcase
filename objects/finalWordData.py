class finalWord:
    def __init__(self, word_one, word_two):
        self.word = ''
        self.word_length = 0
        self.word_one = word_one
        self.word_two = word_two

    def set_word(self, word):
        self.word = word

    def increment_word_length(self):
        self.word_length += 1

