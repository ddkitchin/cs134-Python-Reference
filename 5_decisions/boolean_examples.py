#@ copyright Deborah Kitchin

def main() -> None:
    # boolean statement and boolean statement
    grade = int(input("Enter grade: "))
    if (grade > 79) and (grade < 90):
        print("B")
    else:
        print("not a B")

    # boolean statement or boolean statement
    passport = input("Enter yes if you have a passport: ")
    drivers_license = input("Enter yes if you have a driver's License: ")
    if (passport == "yes") or (drivers_license == "yes"):
        print("You can fly")
    else:
        print("You can't fly: ")

    # not a boolean statement
    done = input("Enter yes when done playing: ")
    if not (done == "yes"):
        print("Keep playing")
    else:
        print("Goodbye")


if __name__ == "__main__":
    main()
