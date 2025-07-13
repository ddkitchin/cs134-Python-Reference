import random
from typing import List


def roll_hex_dice(num_dice: int = 4) -> List[str]:

    hex_values: List[str] = ['0', '1', '2', '3', '4', '5', '6', '7',
                             '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    rolls: List[str] = []
    for i in range(num_dice):
        roll: str = random.choice(hex_values)
        rolls.append(roll)

    return rolls


def hex_to_decimal(hex_string: str) -> int:

    return int(hex_string, 16)


def hex_to_binary(hex_string: str) -> str:

    decimal: int = int(hex_string, 16)
    return bin(decimal)[2:]  # Remove '0b' prefix


def display_conversions(hex_digits: List[str]) -> None:

    hex_string: str = ''.join(hex_digits)
    decimal_value: int = hex_to_decimal(hex_string)
    binary_value: str = hex_to_binary(hex_string)

    print(f"\n{'=' * 50}")
    print(f"HEX DICE ROLL RESULTS")
    print(f"{'=' * 50}")
    print(f"Individual dice: {' '.join(hex_digits)}")
    print(f"Combined hex:    {hex_string}")
    print(f"Decimal value:   {decimal_value:,}")
    print(f"Binary value:    {binary_value}")
    print(f"{'=' * 50}")


def show_conversion_hints(hex_digits: List[str]) -> None:

    hex_string: str = ''.join(hex_digits)

    print(f"\n💡 CONVERSION HINTS 💡")
    print(f"{'=' * 50}")

    # Hex to Decimal hint
    print("🔢 HEX TO DECIMAL:")
    print(f"   {hex_string} = ", end="")
    total: int = 0
    terms: List[str] = []

    for i, digit in enumerate(hex_digits):
        power: int = len(hex_digits) - 1 - i
        digit_value: int = int(digit, 16)
        place_value: int = 16 ** power
        contribution: int = digit_value * place_value
        total += contribution

        if power == 0:
            terms.append(f"{digit}₁₆×1")
        else:
            terms.append(f"{digit}₁₆×16^{power}")

    print(" + ".join(terms))

    # Show the calculation
    print("   = ", end="")
    calc_terms: List[str] = []
    for i, digit in enumerate(hex_digits):
        power: int = len(hex_digits) - 1 - i
        digit_value: int = int(digit, 16)
        place_value: int = 16 ** power
        contribution: int = digit_value * place_value

        if power == 0:
            calc_terms.append(f"{digit_value}×1")
        else:
            calc_terms.append(f"{digit_value}×{place_value}")

    print(" + ".join(calc_terms))
    print(f"   = {total:,}")

    # Binary conversion hint
    print(f"\n🔢 HEX TO BINARY:")
    print("   Each hex digit = 4 binary digits")
    for digit in hex_digits:
        digit_value: int = int(digit, 16)
        binary_4bit: str = format(digit_value, '04b')
        print(f"   {digit} → {binary_4bit}")

    combined_binary: str = ''.join(format(int(d, 16), '04b') for d in hex_digits)
    print(f"   Combined: {combined_binary}")

    # Memory tricks
    print(f"\n🧠 MEMORY TRICKS:")
    print("   A=10, B=11, C=12, D=13, E=14, F=15")
    print("   Place values: ...4096, 256, 16, 1")
    print("   Each hex digit = exactly 4 binary bits")

    # Practice suggestion
    print(f"\n🎯 PRACTICE: Try converting {hex_string} by hand before checking!")
    print(f"{'=' * 50}")


def main() -> None:

    print("🎲 HEX DICE ROLLER 🎲")
    print("Rolling 4 sixteen-sided dice with hex faces (0-F)")
    print("\nCommands:")
    print("  Enter = Roll dice")
    print("  'h' = Show conversion hints")
    print("  'q' = Quit")

    dice_results: List[str] = None

    while True:
        print(f"\n{'>' * 20}")
        if dice_results:
            print("Options: Enter (new roll), 'h' (hints), 'q' (quit):")
        else:
            print("Press Enter to roll dice (or 'q' to quit):")

        user_input: str = input().strip().lower()

        if user_input == 'q':
            print("Thanks for playing! 👋")
            break
        elif user_input == 'h' and dice_results:
            show_conversion_hints(dice_results)
        elif user_input == 'h' and not dice_results:
            print("Roll dice first to see hints!")
        else:
            dice_results = roll_hex_dice(4)

            display_conversions(dice_results)

            print("\nIndividual dice values:")
            for i, hex_val in enumerate(dice_results, 1):
                decimal_val: int = int(hex_val, 16)
                binary_val: str = format(decimal_val, '04b')  # 4-bit binary
                print(f"  Die {i}: {hex_val} (decimal: {decimal_val:2d}, binary: {binary_val})")

            print("\n💡 Type 'h' for step-by-step conversion hints!")


if __name__ == "__main__":
    main()