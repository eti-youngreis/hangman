class Player:

    def __init__(self):
        name = input("Enter your name")
        self.__name = name
        self.__tryings = 0

    def decrees_tryings(self):
        self.__tryings += 1

    def get_name(self):
        return self.__name

    def get_tryings(self):
        return self.__tryings

