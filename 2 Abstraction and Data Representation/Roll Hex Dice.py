import random
from typing import List


def roll_hex_dice(num_dice: int = 4) -> List[str]:
    hex_values: List[str] = ['0', '1', '2', '3', '4', '5', '6', '7',
                             '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    rolls = []
    for i in range(num_dice):
        roll: str = random.choice(hex_values)
        rolls.append(roll)

    return rolls


def display_conversions(hex_digits: List[str]) -> None:
    hex_string = ''.join(hex_digits)

    print(f"{'=' * 50}")
    print(f"HEX DICE ROLL RESULTS")
    print(f"{'=' * 50}")
    print(f"hex: {hex_string}")
    decimal = int(hex_string, 16)
    if input("Show answer. Press enter.") == "":
        print(f"decimal:{int(hex_string, 16)} binary:{bin(decimal)[2:]}")
    print(f"{'=' * 50}")


def main() -> None:
    print("🎲 HEX DICE ROLLER 🎲")
    print("Rolling 4 sixteen-sided dice with hex faces (0-F)")
    print("Commands:")
    print("  Enter = Roll dice")
    print("  'q' = Quit")

    user_input = ""
    while user_input != 'q':
        print(f"\n{'>' * 20}")
        user_input = input("Press Enter to roll dice (or 'q' to quit):").strip().lower()
        if user_input == 'q':
            print("Thanks for playing! 👋")
        else:
            display_conversions(roll_hex_dice(4))


if __name__ == "__main__":
    main()