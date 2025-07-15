# @copyright Deborah Kitchin

def main() -> None:
    name = get_Name()
    address = get_Address()
    player_name = get_player_name()
    privacy = get_privacy()
    print(name)
    print(address)
    print(player_name)
    print(privacy)


def valid_first_name(first: str) -> bool:
    # @return True if first name is not empty

    if len(first) == 0:
        print("ERROR: A first name is required")
        return False
    else:
        return True


def valid_middle_name(middle: str) -> str:
    # @return middle name and a space unless middle name is empty.

    return "FIX ME"



def valid_last_name(first: str, last: str) -> str:
    # @return True is last name is valid otherwise false

    return "FIX ME"


def get_Name() -> str:
    # @return First Middle and Last Name Validated.
    # There should be a space after the first name.

    """ The first name is done for you. You can use this technique for many other
        parts of this assignment... street, city..."""
    first = input("Enter first name ")
    while not valid_first_name(first):  # Notice the call to valid_first_name
        first = input("Enter first name ")

    middle = "FIX ME"  # use valid_middle_name(middle)

    last = "FIX ME"  # use valid_last_name (first,Last) similar to how the first name is done above.

    return first + " " + middle + last


def valid_street(street: str) -> str:
    # @return True if the street is not empty

    return "FIX ME"


def valid_city(city: str) -> str:
    # @return True if the city is not empty

    return "FIX ME"


def valid_state(state: str) -> str:
    # @return True if state is not empty

    return "FIX ME"


def valid_zipcode(zipcode: str) -> str:
    # @return True if zipcode is valid

    return "FIX ME"


def get_Address() -> str:
    # @return valid "street, city state zipcode"

    street = "FIX ME"  # use valid_street (street) similar to how the first name is done above.

    city = "FIX ME"  # use valid_city (city) similar to how the first name is done above

    state = "FIX ME"  # use valid_state (state) similar to how the first name is done above

    zipcode = "FIX ME"  # use valid_zipcode (zipcode) similar to how the first name is done above

    return street + ", " + city + ", " + state + " " + zipcode


def valid_player_name(player_name: str) -> bool:
    # @return True if valid player name.

    return "FIX ME"


def confirm_player_name(player_name: str, player_name2: str) -> bool:
    # @return True if player names match, otherwise False

    return "FIX ME"


def get_player_name() -> str:
    # @return valid player name

    player_name = "FIX ME"  # use valid_player_name (player_name) similar to how the first name is done above

    player_name2 = "FIX ME"  # use confirm_player_name (player_name, player_name2) similar to how the first name is done above

    return "FIX ME"


def valid_privacy(privacy: str) -> bool:
    # @return True if Y or N was selected, otherwise False

    return "FIX ME"


def get_privacy() -> str:
    # @return validated Public or Private visibility.

    return "FIX ME"  # use valid_privacy (privacy) similar to how first name is done above


if __name__ == "__main__":
    main()