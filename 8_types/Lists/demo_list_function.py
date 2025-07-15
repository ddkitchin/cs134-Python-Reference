# @copyright Deborah Kitchin

# noinspection GrazieInspection
def main() -> None:
    # created a list of 3 items
    l = ["a", "b", "c"]
    print("List before function", l)
    # called function with a list as a parameter
    demo_list_function(l)
    print("List after function", l)


# noinspection GrazieInspection
def demo_list_function(l: list) -> None:
    print("\tList in function", l)

    # change first item in a list
    l[0] = "z"
    print("\tList in function after first item changed", l)

    # Create a new list with numbers and set l to new l
    new_l = [1, 2, 3]
    l = new_l
    print("\tList in function after set to new list", l)


if __name__ == "__main__":
    main()
