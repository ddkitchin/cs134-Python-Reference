#  This program turns an integer into its English name using a dictionary.
def main()-> None:
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
def int_name(number:int)->str:

    # The number that still needs to be converted.
    name = ""  # Start name with empty string.

    # If the number is > 100
    # noinspection GrazieInspection,AiaStyle
    if number >= 100:
        # pass the hundreds digit to digit name to get the word.
        name = digitName[number // 100] + " hundred"
        # remove the hundreds digit from number
        number = number % 100

    # if the tens digit is 20 or higher, use the tensName converter and remove the tens digit
    # noinspection GrazieInspection
    if number >= 20:
        name = name + " " + tensName[number // 10]
        number = number % 10
    # if the tens digit is a teen, use the teens converter and you are done.
    elif number >= 10:
        name = name + " " + teenName[number]
        number = 0

    # do the digit conversion
    if number > 0:
        name = name + " " + digitName[number]

    return name

#  @return the digit name
digitName = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

#  @return the teens name
teenName = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

#  @return tens word
tensName = {
    9: "ninety",
    8: "eighty",
    7: "seventy",
    6: "sixty",
    5: "fifty",
    4: "forty",
    3: "thirty",
    2: "twenty"
}

if __name__ == "__main__":
    main()