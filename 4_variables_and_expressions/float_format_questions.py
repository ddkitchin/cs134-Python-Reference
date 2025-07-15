#@copyright Deborah Kitchin

# Constants
NAME = "Penny"  # string
BREED = "Golden Lab"  # string
AGE = 5  # integer
DOG_YEARS_TO_HUMAN_YEARS = 7  # integer
AVERAGE_DOG_LIFE = 15  # integer

def main() -> None:

    human_age = AGE * DOG_YEARS_TO_HUMAN_YEARS  # integer * integer = integer
    dog_life_complete = AGE / AVERAGE_DOG_LIFE  # integer / integer = real number.

    # This is how you should print using f-string according to class style guidelines.
    print(f'My pet {NAME} is a {BREED}. She is {AGE} years old.\nIn human years she is {human_age} and has completed about {dog_life_complete:.2f} of their life.')

    # This is the way we did it in class before Python 3.6
    print()  # blank line
    print('My pet %s is a %s. She is %d years old.\nIn human years she is %d and has completed about %.2f of their life.' % (
            NAME, BREED, AGE, human_age, dog_life_complete))

    # fields with no text between values
    # Using round and 2 digit precision.

    print()  # Print blank line
    print(NAME, BREED, AGE, human_age, round(dog_life_complete, 2))


if __name__ == '__main__':
    main()
