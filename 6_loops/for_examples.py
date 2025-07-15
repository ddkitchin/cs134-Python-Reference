#@copyright Deborah Kitchin

def main() -> None:
    # for loop that goes through each character in a string.
    name = "Debbie"
    for letter in name:
        print(letter)

    # An alternative for loop that goes through each character in a string.
    # Uses the variable i as the index variable.
    for i in range(0, len(name)):
        print(name[i])

    # A while loop that goes through each character in a string using an index.
    # It does the same thing as both of the for loops above.
    i = 0
    while i < len(name):
        print(name[i])
        i = i + 1

    # for loop that prints evens from 0-50
    for x in range(0, 51, 2):
        print(x)


if __name__ == "__main__":
    main()
