# @copyright Deborah Kitchin

def main() -> None:
    price = float(input("Enter price: "))

    if price < 28:
        discount = .92  # 8% discount
    else:
        discount = .84  # 16% discount

    final_price = price * discount

    print(f'Final price is ${final_price:.2f}.')


if __name__ == "__main__":
    main()