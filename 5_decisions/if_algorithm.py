#@copyright Deborah Kitchin

def main() -> None:
    birth_month = int(input("Enter your month "))
    check_date1 = 0
    check_date2 = 0

    # noinspection SpellCheckingInspection
    '''If the month is January, February, or March, you make less checks with Algorithm 1
        than if you use Algorithm 2. For all other months you make less checks with 
        Algorithm 2. 
        
        Algorithm 1 has right drift. Algorithm 3 shows same algorithm as Algorithm 1,
        but with Python elif keyword instead of the Python else if. Algorithm 3 
        can not count the decisions because the else and if are combined into the elif.'''

    print("Algorithm 1 ", end="")
    check_date1 += 1
    if birth_month == 1:
        print("January ", check_date1, " check")
    else:
        check_date1 += 1
        if birth_month == 2:
            print("February ", check_date1, " checks")
        else:
            check_date1 += 1
            if birth_month == 3:
                print("March ", check_date1, " checks")
            else:
                check_date1 += 1
                if birth_month == 4:
                    print("April ", check_date1, " checks")
                else:
                    check_date1 += 1
                    if birth_month == 5:
                        print("May ", check_date1, " checks")
                    else:
                        check_date1 += 1
                        if birth_month == 6:
                            print("June ", check_date1, " checks")
                        else:
                            check_date1 += 1
                            if birth_month == 7:
                                print("July ", check_date1, " checks")
                            else:
                                check_date1 += 1
                                if birth_month == 8:
                                    print("August ", check_date1, " checks")
                                else:
                                    check_date1 += 1
                                    if birth_month == 9:
                                        print("September ", check_date1, " checks")
                                    else:
                                        check_date1 += 1
                                        if birth_month == 10:
                                            print("October ", check_date1, " checks")
                                        else:
                                            check_date1 += 1
                                            if birth_month == 11:
                                                print("November ", check_date1, " checks")
                                            else:
                                                print("December ", check_date1, " checks")

    print("Algorithm 2 ", end="")
    check_date2 += 1
    if birth_month < 7:
        check_date2 += 1
        if birth_month < 4:
            check_date2 += 1
            if birth_month < 2:
                print("January ", check_date2, " checks")
            else:
                check_date2 += 1
                if birth_month < 3:
                    print("February ", check_date2, " checks")
                else:
                    print("March ", check_date2, " checks")
        else:
            check_date2 += 1
            if birth_month < 5:
                print("April ", check_date2, " checks")
            else:
                check_date2 += 1
                if birth_month < 6:
                    print("May ", check_date2, " checks")
                else:
                    print("June ", check_date2, " checks")
    else:
        check_date2 += 1
        if birth_month < 10:
            check_date2 += 1
            if birth_month < 8:
                print("July ", check_date2, " checks")
            else:
                check_date2 += 1
                if birth_month < 9:
                    print("August ", check_date2, " checks")
                else:
                    print("September ", check_date2, " checks")
        else:
            check_date2 += 1
            if birth_month < 11:
                print("October ", check_date2, " checks")
            else:
                check_date2 += 1
                if birth_month < 12:
                    print("November ", check_date2, " checks")
                else:
                    print("December ", check_date2, " checks")

    ''' Algorithm 1 and 3 ARE THE SAME ALGORITHM. You are using different python
    syntax (Algorithm 1 is if...else...if....else 
    versus Algorithm 2 is if...elif...elif...elif...)
    so they look different but they are the same algorithm.'''

    print("Algorithm 3 ", end="")

    if birth_month == 1:
        print("January ")
    elif birth_month == 2:
        print("February ")
    elif birth_month == 3:
        print("March ")
    elif birth_month == 4:
        print("April ")
    elif birth_month == 5:
        print("May ")
    elif birth_month == 6:
        print("June ")
    elif birth_month == 7:
        print("July ")
    elif birth_month == 8:
        print("August ")
    elif birth_month == 9:
        print("September ")
    elif birth_month == 10:
        print("October ")
    elif birth_month == 11:
        print("November ")
    else:
        print("December ")


if __name__ == "__main__":
    main()
