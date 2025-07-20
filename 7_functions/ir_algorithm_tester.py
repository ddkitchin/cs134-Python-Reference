#@ copyright Deborah Kitchin
def main() -> None:

    answers = ["January", "Feburary", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
    
    for month in range (12):
        print(f'Correct Answer for {month+1:03d} is {answers[month]:11} Student Answer:', end=" ")
        tester(month+1)

    print(f'Correct Answer for {0:03d} is {"**Nothing**":11} Student Answer:', end=" ")
    tester(0)
    print(f'Correct Answer for {-1:03d} is {"**Nothing**":11} Student Answer:', end=" ")
    tester(-1)
    print(f'Correct Answer for {50:03d} is {"**Nothing**":11} Student Answer:', end=" ")
    tester(50)
    print(f'Correct Answer for {"a":3} is {"**Nothing**":11} Student Answer:', end=" ")
    tester("a")
    print(f'Correct Answer for {"3.4":03} is {"**Nothing**":11} Student Answer:', end=" ")
    tester(3.4)

def tester(month:int) -> None:
    ## place student code here

    # check if integer is passed
    #if not isinstance(month,int): # not pythonic
    #    print()
    # check if integer is value 1 to 12
    #elif not (1 <= month <= 12):
    #    print()
    # uncomment above and make elif
    if month == 1:
        print("January")
    else:
        if month == 2:
            print("February")
        else:
            if month == 3:
                print("March")
            else:
                if month == 4:
                    print("April")
                else:
                    if month == 5:
                        print("May")
                    else:
                        if month == 6:
                            print("June")
                        else:
                            if month == 7:
                                print("July")
                            else:
                                if month == 8:
                                    print("August")
                                else:
                                    if month == 9:
                                        print("September")
                                    else:
                                        if month == 10:
                                            print("October")
                                        else:
                                            if month == 11:
                                                print("November")
                                            else:
                                                print("December")

if __name__ == "__main__":
    main()
