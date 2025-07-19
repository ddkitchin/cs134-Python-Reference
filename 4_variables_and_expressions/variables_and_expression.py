# @copyright Deborah Kitchin
# import math library
from math import *


def main() -> None:
    # if you use the line below instead of the line above all math functions must be proceeded by math.
    # import math
    # print (math.pi)

    # Naming Conventions and simple variable manipulation

    # String variable
    favorite_game = input("Enter favorite game: ")

    # Integer variable
    favorite_number = int(input("Enter favorite number: "))

    # Real variable
    favorite_price = float(input("Enter your favorite price: "))

    print(
        f"My favorite game is {favorite_game}. My favorite number is {favorite_number}. My favorite price is {favorite_price:.2f}.")

    print()
    # Using math library.
    # zybooks shows this DO NOT USE .format
    print('pi is {:.4f}'.format(pi))

    # instead USE fstring. It is more "pythonic" and similar to how other languages do it.
    print(f'pi is {pi:.4f}')

    print()

    '''
    1) How to get number values from the user.
    2) How to use a math function. 
    3) How to format a complex message.
    4) How to add 2 numbers together
    5) How to create an accumulator
    '''
    number1 = int(input("Enter an integer:"))  # 1) input number
    number2 = float(input("Enter a real number: "))
    print(
        f"The square root of {number1:d} is {sqrt(number1):.4f}.")  # 2&3  use math function and format complex message
    print(f"The square root of {number2:.4f} is {sqrt(number2):.4f}.")
    total = number1 + number2  # add two numbers
    print(f"The sum of {number1:.4f} is {number2:.4f} is {total:.4f}.")
    total = total + 1  # 5 accumulator
    print(f"Total is now {total:.4f}.")

    print()
    '''
    1) How to show individual letters in string.
    2) How to repeat characters in display
    3) How to use lower, upper and replace with a string.
    '''
    name = input("Enter a name: ")

    print(f"\n{10 * '='} Name={name} {10 * '='}")

    ''' 0 position is first letter len(name) - 1 is last position '''
    print(f"The first letter is {name[0]} and the last letter is {name[-1]}.")

    name_all_caps = name.upper()
    print(f"Name all caps {name_all_caps}.")
    print(f"Name all caps {name.upper()}.")

    name_lower = name.lower()
    print(f"Name lowercase {name_lower}.")
    print(f"Name lowercase {name.lower()}.")

    name_replaced = name.replace("y", "ie")
    print(f"Name replaced  {name_replaced}.")
    print(f"Name replaced  {name.replace('y', 'ie')}.")

    print("=" * 30)
    print(f"\n{10 * '='} Last Demos {10 * '='}")

    ''' A little more formatting.
    1) How to use ascii and escape sequence to do a tab.
    2) How to print a unicode symbol. '''
    print(f"number 1\u0009\tnumber 2")  #results are the same for this line and
    print(f' {number1}\t\t\t{number2}')  # this line.
    print("The unicode pi symbol is \u03A0.")

    print("*" * 50)
    ''' How to get a string, integer, and float. Manipulate them and print them.
    Input dog name, age, and weight.'''
    dog_name = input("Enter the dog's name: ")
    age = int(input("Enter the dog's age: "))
    weight = float(input("Enter the dog's weight: "))

    print(f"The dog's name is {dog_name}.")
    print(f'Dog age: {age}.')
    print(f'Dog weight = {weight:.2f}.')
    human_years = age * 7
    print(f'The dog {dog_name} is {age} years old and is {human_years} in human years.')


if __name__ == "__main__":
    main()