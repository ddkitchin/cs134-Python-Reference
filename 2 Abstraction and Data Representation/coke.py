# @copyright Deborah Kitchin

def main() -> None:
    # string literal between the ""
    print("Coke Selected")

    price = 1
    print(f"Price = {price:.2f}")

    tax = .10
    print(f'Tax = {tax:.2f}')

    total_price = price + tax
    print(f'Total = {total_price:.2f}')


if __name__ == "__main__":
    main()
