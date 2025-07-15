# @copyright Deborah Kitchin
def main() -> None:
    initial_balance = 10000
    rate = 4
    years = 3
    print(f'In {years} years at {rate}%, ${initial_balance:,} will be ${future_value(initial_balance, rate, years):,.2f}.')

    initial_balance = 5000
    rate = 3.5
    years = 4
    print(f'In {years} years at {rate}%, ${initial_balance:,} will be ${future_value(initial_balance, rate, years):,.2f}.')

    initial_balance = 1000
    rate = 10
    years = 1
    print(f'In {years} years at {rate}%, ${initial_balance:,} will be ${future_value(initial_balance, rate, years):,.2f}.')

    initial_balance = int(input("Enter initial balance: "))
    rate = float(input("Enter rate: "))
    years = int(input("Enter years: "))
    print(f'In {years} years at {rate}%, ${initial_balance:,} will be ${future_value(initial_balance, rate, years):,.2f}.')


#  @return the future value of the investment
def future_value(initial_balance: int, rate: float, years: int) -> float:
    return initial_balance * (1 + rate / 100) ** years


if __name__ == "__main__":
    main()
