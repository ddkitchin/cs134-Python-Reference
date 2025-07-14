# @copyright Deborah Kitchin

def main() -> None:  # Include in all programs. Defines the function in the main. We will learn more about this later.
    # Hello World
    print("Hello World")

    ''' Show a variable in a sentence '''
    my_name = 'Debbie'
    print(f"The value for the variable name is a portal for {my_name}.")

    # Add an age to the sentence
    my_age = 57
    print(f"Hello, My name is {my_name} and I'm {my_age} years old.")

    # blank line
    print()

    # Description of Eric Idle
    first_name = "Eric"
    last_name = "Idle"
    age = 74
    profession = "comedian"
    affiliation = "Monty Python"

    # \n will print a blank line after the sentence.
    print(
        f"Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}.\n")

    # Calculated values
    print(f"{first_name} is {age - my_age} older than {my_name}")


# This decision (if statement) checks to see if the program is being run from this
# program or referenced from another program. We will learn more about this later.
if __name__ == "__main__":  # Include in all programs. Checks to see if running from this program.
    main()  # Include in all programs. Calls the main function.
