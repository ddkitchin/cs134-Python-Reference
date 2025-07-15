#@copyright Deborah Kitchin
# Define Lists

# noinspection GrazieInspection,SpellCheckingInspection
def main() -> None:
    values = []  # empty list
    print("values=", values)

    # list of month numbers --- notice month 1 is index0
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print("months=", months)
    print("First month number is", months[0])

    # list of students in class
    # noinspection SpellCheckingInspection
    roster = ["Archie", "Nancy", "Amber", "Aricke", "Dylan", "Jeffery", "AJ"]
    print("roster", roster)

    # list of grades
    grades = [90, 95, 85, 75, 65, 100]
    print("grades", grades)

    # Traverse list 3 ways
    print("*" * 20, "Option 1: Go through list", "*" * 20)
    for student in roster:
        print(student)
    print()

    print("*" * 20, "Option 2: Go through list", "*" * 20)
    for i in range(len(roster)):
        # end=" " will cause print to stay on the same line and put a space after the item printed.
        print(roster[i], end=" ")
    print()

    print("*" * 20, "Option 3: Use enumerate to go through list", "*" * 20)
    for studentNumber, studentValue in enumerate(roster):
        print(studentNumber, studentValue)
    print()

    # Access specific item in the list
    print("Print 3rd item:", roster[2])
    print("Print last item:", roster[-1])
    print("Print first item using last:", roster[-1 * len(roster)])

    # list of person's favorite things
    # The programmer must know the structure of the data to do this.
    my_favorites = ["Debbie", "Pink", 8, "Mario"]
    your_favorites = ["Barbra", "Blue", 24, "GTA"]

    # Access list of various things
    print("List of various things:", end="")
    print(
        f"{my_favorites[0]}'s favorite color is {my_favorites[1]}, favorite number is {my_favorites[2]}, and favorite character {my_favorites[3]}.")
    print(
        f"{your_favorites[0]}'s favorite color is {your_favorites[1]}, favorite number is {your_favorites[2]}, and favorite character {your_favorites[3]}.")

    # Concatenate 2 list
    all_favorites = my_favorites + your_favorites
    print(all_favorites)


if __name__ == "__main__":
    main()
