# @copyright Deborah Kitchin

from random import randint


def main() -> None:
    # Guess the number game. You can play as long as you want
    keep_going = True
    games = 0  # counts how many games are played
    wins = 0  # counts how many games are won
    guess = 0
    while keep_going:
        games = games + 1
        print("You have 3 tries to guess the number")
        actual_number = randint(1, 10)
        print(actual_number)  # uncomment to help with testing
        for i in range(0, 3):
            guess = int(input("Pick a number between 1 and 10 "))
            if guess == actual_number:
                wins = wins + 1
                print("You win!")
                break
        if guess != actual_number:
            print("You lose. The number is ", actual_number)
        ''' keep_going is a boolean. I am setting it by asking
        the user for input, converting it to upper, and checking to see if
        that input is equal to Y. When it is Y keep_going is True, otherwise False.
        boolean equal x == y is the formula '''
        keep_going = input("Do you want to keep going Y/N ").upper() == "Y"

    print("You played", games, "games and won", wins, "games.")


if __name__ == "__main__":
    main()
