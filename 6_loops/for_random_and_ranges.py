#@copyright Deborah Kitchin

# noinspection GrazieInspection
"""Don't confuse the for loop range(start,end) with the
randint(start,end) results.

The for loop range(0,MAX_NUMBERS) stops before the
limit, in this case, MAX_NUMBERS stops at 4, not 5.

The randint function(0,MAX_NUMBERS), stops at 5."""

from random import *

# Constants
MAX_NUMBERS = 5

def main() -> None:
    print("Random Reals")
    for i in range(MAX_NUMBERS):
        print("Iteration=", i, end="")
        random_value = random()
        print(" Random Value =", random_value)
    print("Random Integers")
    for i in range(MAX_NUMBERS):
        print("Iteration=", i, end="")
        random_value = randint(0, MAX_NUMBERS)
        print(" Random Value =", random_value)


if __name__ == "__main__":
    main()
