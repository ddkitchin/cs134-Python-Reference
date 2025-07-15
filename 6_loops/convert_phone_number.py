""" Algorithm

get alphanumeric phone number
set newNumber to empty string
for every character in the phone number
    convert alphabetic characters to a number
    append the number to new number
print new number
"""


def main() -> None:
    phone_number = input("Enter a phone number: ")
    new_number = ""

    print("Original number", phone_number)
    print(new_number)

    for character in phone_number:
        #FIX ME
        #print("not done")
        #print("line 10",character)
        if character.upper() == "A" or character.upper() == "B" or character.upper() == "C":
            new_number = new_number + "2"
        elif character.upper() == "D" or character.upper() == "E" or character.upper() == "F":
            new_number = new_number + "3"
        elif character.upper() == "G" or character.upper() == "H" or character.upper() == "I":
            new_number = new_number + "4"
        elif character.upper() == "J" or character.upper() == "K" or character.upper() == "L":
            new_number = new_number + "5"
        elif character.upper() == "M" or character.upper() == "N" or character.upper() == "O":
            new_number = new_number + "6"
        elif character.upper() == "P" or character.upper() == "Q" or character.upper() == "R" or character.upper() == "S":
            new_number = new_number + "7"
        elif character.upper() == "T" or character.upper() == "U" or character.upper() == "V":
            new_number = new_number + "8"
        #else:
        elif character.upper() == "W" or character.upper() == "X" or character.upper() == "Y" or character.upper() == "Z":
            new_number = new_number + "9"
        else:
            new_number = new_number + character

    print("final new number", new_number)


if __name__ == "__main__":
    main()
