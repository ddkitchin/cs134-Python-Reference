##
#  This program reads a sequence of values and prints them, marking the largest value.
#

def main() -> None:
    # Create an empty list.
    values = []

    # Read the input values.
    user_input = input("Please enter values, Q to quit: ")
    while user_input.upper() != "Q":
        values.append(float(user_input))
        user_input = input("Please enter values, Q to quit: ")

    if len(values) > 0:
        process_list(values)


def process_list(values: list) -> None:
    # Find the largest value.
    largest = values[0]
    for i in range(1, len(values)):
        if values[i] > largest:
            largest = values[i]

    # Print all values, marking the largest.
    for element in values:
        print(element, end="")
        if element == largest:
            print(" <== largest value", end="")
        print()


if __name__ == "__main__":
    main()
