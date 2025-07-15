#@copyright Deborah Kitchin

def main() -> None:
    students = ["John", "Bob", "Nancy"]  # list
    print(students)
    print(f'The class is {type(students)}.')

    month_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)  # tuple
    print(month_numbers)
    print(f'The class is {type(month_numbers)}.')

    hand = {"Ace", "King", "Queen", "Jack"}  #set
    print(hand)
    print(f'The class is {type(hand)}.')

    # noinspection SpellCheckingInspection
    words = {"hello": "bonjour", "goodbye": "adieu", "bathroom": "toilet",
             "Please": "S'il vous plait", "Thank You": "Merci"}  # dictionary
    print(words)
    print(f'The class is {type(words)}.')


if __name__ == "__main__":
    main()
