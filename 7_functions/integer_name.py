#  This program turns an integer into its English name.
def main() -> None:
    keep_going = True
    while keep_going:
        value = int(input("Please enter a positive integer < 1000: "))
        if 0 < value < 1000:
            print(int_name(value))
        else:
            print("Please enter a number between 1 and 999.")
        keep_going = input("Do you want to keep going Y/N ")[0].upper() == "Y"


#  @return the name of the number (e.g. "two hundred seventy-four")
# noinspection GrazieInspection,AiaStyle
def int_name(number: int) -> str:
    # The number that still needs to be converted.
    name = ""  # Start name with empty string.

    # If the number is > 100
    # noinspection GrazieInspection,AiaStyle
    if number >= 100:
        # Pass the hundreds digit to digit name to get the word.
        name = digit_name(number // 100) + " hundred"
        # remove the hundreds digit from number
        number = number % 100

    # If the tens digit is 20 or higher, use the tens converter and remove the tens digit
    # noinspection GrazieInspection
    if number >= 20:
        name = name + " " + tens_name(number)
        number = number % 10
    # If the tens digit is a teen, use the teens converter and you are done.
    elif number >= 10:
        name = name + " " + teen_name(number)
        number = 0

    # Do the digit conversion
    if number > 0:
        name = name + " " + digit_name(number)

    return name


#  @return the digit name
def digit_name(number: int) -> str:
    if number == 1: return "one"
    if number == 2: return "two"
    if number == 3: return "three"
    if number == 4: return "four"
    if number == 5: return "five"
    if number == 6: return "six"
    if number == 7: return "seven"
    if number == 8: return "eight"
    if number == 9: return "nine"
    return ""


#  @return the teens name
def teen_name(number: int) -> str:
    if number == 10: return "ten"
    if number == 11: return "eleven"
    if number == 12: return "twelve"
    if number == 13: return "thirteen"
    if number == 14: return "fourteen"
    if number == 15: return "fifteen"
    if number == 16: return "sixteen"
    if number == 17: return "seventeen"
    if number == 18: return "eighteen"
    if number == 19: return "nineteen"
    return ""


#  @return tens name
def tens_name(number: int) -> str:
    if number >= 90: return "ninety"
    if number >= 80: return "eighty"
    if number >= 70: return "seventy"
    if number >= 60: return "sixty"
    if number >= 50: return "fifty"
    if number >= 40: return "forty"
    if number >= 30: return "thirty"
    if number >= 20: return "twenty"
    return ""


if __name__ == "__main__":
    main()
