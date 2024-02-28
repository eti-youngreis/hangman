class Sentence:

    def __init__(self, sentence):
        self.__sentence = sentence
        self.__hide_sentence = ['-' if c != ' ' else ' ' for c in self.__sentence]

    def get_sentence(self):
        return self.__sentence

    def get_hide_sentence(self):
        return self.__hide_sentence

    def get_hide_sentence_string(self):
        return ''.join(self.__hide_sentence)

    def __str__(self):
        str_to_print = ''
        for i in self.get_hide_sentence_string():
            str_to_print += i + ' '
        return str_to_print

    def is_exist(self, choice):
        return choice in self.__sentence

    def replace_letter(self, choice):
        for i in range(len(self.__sentence)):
            if self.__sentence[i] == choice:
                self.__hide_sentence[i] = choice
