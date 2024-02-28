from game import Game


def main():
    is_want_to_play = int(input("Enter 1 to play, else 0"))
    while is_want_to_play:
        game = Game()
        is_want_to_play = int(input("Enter 1 to play, else 0"))


if __name__ == '__main__':
    main()
