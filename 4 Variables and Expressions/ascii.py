# @copyright Deborah Kitchin

def main() -> None:
    # Set variable character to a space.
    character = " "
    # Keep going while the variable character is not an empty string.
    while character != "":
        # print the ascii value of the character entered
        # Notice used " on outside of f-string and ' to put actual ' around the ascii value
        print(f"The ASCII value of '{character}' is {ord(character)}.")
        character = input("Enter a character ")

    # Set ascii_value to 100 to force the program into the loop. The value can be anything as long as it is >= 0

    ascii_value = 100
    while ascii_value >= 0:
        # Print the character value of the ascii entered
        # Notice used ' on outside of f-string and \' to put actual ' around the ascii value.
        # The \ is an escape character to tell the compiler to treat the value as just a plan
        # character ... not the end of the string.
        print(f'The character value of {str(ascii_value)} is \'{chr(ascii_value)}\'')
        ascii_value = int(input("Enter an ascii value "))


if __name__ == "__main__":
    main()
