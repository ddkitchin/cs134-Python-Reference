#@copyright Deborah Kitchin
def main()->None:
    game102_class=set()
    python_class=set()

    more_students=True
    while more_students:
        student_name=input("Enter a student in game 102 ")
        if student_name != "":
            game102_class.add(student_name)
        else:
            more_students=False

    more_students=True
    while more_students:
        student_name=input("Enter a student in python ")
        if student_name != "":
            python_class.add(student_name)
        else:
            more_students=False

    print("Game class ",game102_class)
    print("Python class ",python_class)
    print("Union ",game102_class.union(python_class))
    print("Intersection ",game102_class.intersection(python_class))
    print("Difference",game102_class.difference(python_class))

if __name__ == "__main__":
    main()