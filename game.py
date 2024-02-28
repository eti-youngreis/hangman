from random import random

from player import Player
from sentence import Sentence


class Game:
    MAX_TRYINGS = 5
    file_score = open('high_score.txt', 'r')
    file_value = file_score.read()
    file_score.close()
    if file_value == '':
        file_score = open('high_score.txt', 'w')
        file_score.write(str(MAX_TRYINGS))
        file_score.close()
        file_score = open('high_score.txt', 'r')
        file_value = file_score.read()
    MIN_TRYINGS = int(file_value)
    SENTENCES = open('sentences.txt').read().splitlines()
    RANDOM = random()

    def __init__(self):
        self.__player = Player()
        self.__sentence = Sentence(Game.SENTENCES[int(Game.RANDOM * len(Game.SENTENCES))])
        self.game_progress()

    def is_game_over(self):
        return self.__player.get_tryings() >= Game.MAX_TRYINGS or self.is_win()

    def is_win(self):
        return '-' not in self.__sentence.get_hide_sentence()

    @staticmethod
    def is_valid_choice(choice):
        return str.isalpha(choice)

    def choose_letter(self):
        letter = input('Enter your choice')
        if Game.is_valid_choice(letter):
            if not self.__sentence.is_exist(letter):
                self.__player.decrees_tryings()
            else:
                self.__sentence.replace_letter(letter)

    def print_tryings(self):
        print(f'Number of failures {self.__player.get_tryings()}')
        if self.__player.get_tryings() < int(Game.MIN_TRYINGS):

            file = open('high_score.txt', 'w')
            file.write(str(self.__player.get_tryings()))
            file.close()
            print('your number of failures is minimal!!!!')

    def turn(self):
        self.choose_letter()

    def game_progress(self):
        while not self.is_game_over():
            print(self.__sentence)
            self.turn()
        if self.is_win():
            print(self.__sentence)
            print(f'{self.__player.get_name()} win!!!')
            self.print_tryings()
        else:
            print(f'Game Over!\nThe sentence is: {self.__sentence.get_sentence()}')
