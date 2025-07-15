#@copyright Deborah Kitchin

from random import randint


def main() -> None:
    while "Y" == input("Do you want to keep going? ").upper():
        string = input("Enter a string ")
        print(f"String is {string}")
        length = len(string)
        print(f"The length of the string is {length}")
        # Notice that on iteration 1, the index is 0 and the character in the 1st position
        # is printed. The loop starts at the 0 index and stops before the value of length,
        for index in range(0, length):
            print(f"index={index} and character is {string[index]}", end="")
            print(f".\tRandom character is {string[randint(0, length - 1)]}")


if __name__ == "__main__":
    main()
