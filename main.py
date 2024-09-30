from game import Game


def main():
    want_to_play = int(input("Enter 1 to play, else 0"))
    while want_to_play:
        game = Game()
        want_to_play = int(input("Enter 1 to play, else 0"))


if __name__ == '__main__':
    main()
