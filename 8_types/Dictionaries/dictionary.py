#@copyright Deborah Kitchin
def main() -> None:
    # Note: I am using a variable name nameKey. This is not very "pythonic".
    # In python you don't want to name variables with an indication of the type.
    # Python is a typeless language.

    # Create a dictionary
    # noinspection SpellCheckingInspection
    words = {"hello": "bonjour", "goodbye": "adieu", "bathroom": "toilet",
             "please": "s'il vous plait", "thank You": "merci"}

    # Get the value of a key in the dictionary
    print(words)
    word_key = "hello"
    print(f'{word_key.capitalize()} translates to {words[word_key]}')

    # Add a new item to the dictionary
    print("=" * 25)
    word_key = "yes"
    word = input(f"Enter the french word for {word_key} ")
    words[word_key] = word

    # Go through all the items in the dictionary
    print("=" * 25)
    for word_key in words:
        print(f'{word_key:<15}translates to\t\t{words[word_key]}')

    # Delete an item in the dictionary with a pop.
    print("=" * 25)
    word_key = input("Enter the english word to delete ")
    answer = words.pop(word_key)
    print(f'The key {word_key} with the value {answer} was deleted')
    for word_key in words:
        print(f'{word_key} translates to {words[word_key]}')

    # Delete an item in the dictionary with a del.
    print("=" * 25)
    word_key = input("Enter the english word to delete ")
    del words[word_key]
    for word_key in words:
        print(f'{word_key} translates to {words[word_key]}')

    # Check if a key is in the dictionary
    print("=" * 25)
    word_key = "starter"
    while word_key != "":
        if word_key in words:
            print(f'{word_key} translates to {words[word_key]}')
        else:
            print(f'{word_key} is not in the dictionary')
        word_key = input(f'Enter a word to look up ')

    # Morse code dictionary.
    morse_code = {"A": ".-", "N": "-.", "0": "-----",
                 "B": "-...", "O": "---", "1": ".----",
                 "C": "-.-.", "P": ".--.", "2": "..---",
                 "D": "-..", "Q": "--.-", "3": "...--",
                 "E": ".", "R": ".-.", "4": "....-",
                 "F": "..-.", "S": "...", "5": ".....",
                 "G": "--.", "T": "-", "6": "-....",
                 "H": "....", "U": "..-", "7": "--...",
                 "I": "..", "V": "...-", "8": "---..",
                 "J": ".---", "W": ".--", "9": "----.",
                 "K": "-.-", "X": "-..-", ".": ".-.-.-",
                 "L": ".-..", "Y": "-.--", ",": "--..--",
                 "M": "--", "Z": "--..", "?": "..--.."}

    print(morse_code)

    from operator import itemgetter
    print(sorted(morse_code.items(), key=itemgetter(0)))

    name = "Debbie"
    print(morse_code["D"])
    while name != "":
        print(f'{name} is ', end="")
        for char in name.upper():
            print(morse_code[char], " ", end="")
        print()
        name = input("Enter another word ")


if __name__ == "__main__":
    main()
