# @copyright Deborah Kitchin

# Set the constant. Try, 3, -1, 10.
LIMIT = 3

def main()-> None:
    # Set i to a value. Try 1, 3, 0, 4, and 10.
    i = 1

    # How many times is while boolean tested?
    # noinspection GrazieInspection,SpellCheckingInspection
    while i <= LIMIT:
        print(f'i = {i}')
        # noinspection SpellCheckingInspection
        i = i + 1  # This is a valid accumulator and the same result as the next line.
        # i += 1 # This is a valid accumulator and the same result as the previous line.

    print("finished")
    print(f'i = {i}')


if __name__ == "__main__":
    main()
