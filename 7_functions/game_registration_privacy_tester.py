from game_registration_privacy import *

def main() -> None:

    wrong = False
    print("=============valid_privacy(privacy)==============")
    print("Show error message when Privacy empty")
    assert valid_privacy("") == False, f'valid_privacy("") expected False got: {valid_privacy("")}'
    print("Show error message when Privacy q")
    assert valid_privacy("q") == False, f'valid_privacy("q") expected False got: {valid_privacy("q")}'
    print("Privacy Y")

    assert valid_privacy("Y") == True, f'valid_privacy("Y") expected True got: {valid_privacy("Y")}'

    if valid_privacy("Yes"):
        print("Privacy Yes")
    else:
        wrong = True
        print("Privacy Yes ******STUDENT ANSWER WRONG*****")
        print(f'valid_privacy("Yes") expected True got: {valid_privacy("Yes")}')

    print("Privacy y")
    assert valid_privacy("y") == True, f'valid_privacy("y") expected True got: {valid_privacy("y")}'

    if valid_privacy("yes"):
        print("Privacy yes")
    else:
        wrong = True
        print("Privacy yes ******STUDENT ANSWER WRONG*****")
        print(f'valid_privacy("yes") expected True got: {valid_privacy("yes")}')

    print("Privacy N")
    assert valid_privacy("N") == True, f'valid_privacy("N") expected True got: {valid_privacy("N")}'

    if valid_privacy("No"):
        print("Privacy No")
    else:
        wrong = True
        print("Privacy No ******STUDENT ANSWER WRONG*****")
        print(f'valid_privacy("No") expected True got: {valid_privacy("No")}')

    print("Privacy n")
    assert valid_privacy("n") == True, f'valid_privacy("n") expected True got: {valid_privacy("n")}'

    if valid_privacy("no"):
        print("Privacy no")
    else:
        wrong = True
        print("Privacy no ******STUDENT ANSWER WRONG*****")
        print(f'valid_privacy("no") expected True got: {valid_privacy("no")}')

    if wrong:
        print(
            "Canvas for privacy: Yes, yes, no, and No are also valid. Anything with Y, y, n, or n in the first character is valid,")


if __name__ == "__main__":
    main()