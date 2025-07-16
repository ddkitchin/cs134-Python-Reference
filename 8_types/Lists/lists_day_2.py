#@copyright Deborah Kitchin

from random import randint

# noinspection GrazieInspection,SpellCheckingInspection
def main() -> None:
    # noinspection SpellCheckingInspection
    roster = ["Nathan", "Nancy", "Amber", "Aricke", "Dylan", "Jeffery", "AJ", "Kelsey"]
    print(roster)

    # Add an item to the end of the list
    roster.append("John")
    print(roster)

    # Add an item to a specific place in the list
    roster.insert(3, "Adrian")
    print(roster)

    # Find an item in the list
    student = input("Enter a student name ")
    if student in roster:
        print(f"{student} is in class")
        #print name with student number which is 1 plus the index.
        print(f"{student}'s class number is {roster.index(student) + 1}")
    else:
        print(f"{student} is not in class")

    # Remove a specific item in a list by index (del), by value (remove), and by position (pop)
    print(f'roster {roster}')
    del roster[3]
    print(f'roster after del [3] {roster}')
    roster.remove("Nathan")
    print(f'roster after remove("Nathan") {roster}')
    roster.pop(2)
    print(f'roster after pop(2) {roster}')

    # Sum, min and max
    grades = [90, 95, 85, 75, 65, 100]
    print("grades", grades)

    # Notice grades does not change with sum, max, and min.
    print("Sum of grades =", sum(grades))
    print("Max of grades =", max(grades))
    print("Min of grades =", min(grades))

    # sort changes the list
    ''' When you do set a list = to another this, it does not create separate copies
    of the list. Each list points to the reference of the same list. For instance:
    uncomment the line below and the last print line in this section'''
    #unsortedGrades = grades   # Both point to (referencing) the same list
    # noinspection SpellCheckingInspection
    '''Now, Comment line directly above and uncomment line directly below to 
           demonstrate how to create 2 separate lists that are independent of each other'''
    #unsortedGrades = grades.copy() # causes second independent list to be created.
    '''results in both variables grades and sortedGrade being sorted'''
    print("grades before sort=", grades)
    grades.sort()
    print("grades after sort=", grades)
    #print("unsortedGrades=",unsortedGrades)

    # Slices
    print("Drop 2 Lowest Grades=", grades[2:len(grades)])

    # Swapping. You have to hold a field so you don't
    # write over it.
    hold = roster[-1]
    roster[-1] = roster[1]
    roster[1] = hold
    print(roster)

    # Tuple example DOES NOT CHANGE AFTER DEFINED May see this, but not expected to use.
    # noinspection SpellCheckingInspection
    roster_tuple = ("Debbie", "Nancy", "Amber", "Aricke", "Dylan", "Jeffery", "AJ")
    print(roster_tuple)

    store_sales = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # I have 10 store_s

    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]

    # I have a table of 10 store_s with sales for each of the 12 months.
    month_sales = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    print(store_sales)
    print(months)
    print(month_sales)
    store_total = 0
    company_total = 0
    for store in range(len(store_sales)):
        print("=" * 18, "Store", store_sales[store], "=" * 18)
        for month in range(len(months)):
            month_sales[store][month] = randint(0, 100000)
            store_total = store_total + month_sales[store][month]
            print(f"\t\t\t{months[month]:10} {month_sales[store][month]:10}")
        print(f"\t\tStore Total {store_total:17}")
        company_total = company_total + store_total
        store_total = 0
    print(f"\tCompany Total {company_total:23}")

if __name__ == "__main__":
    main()
