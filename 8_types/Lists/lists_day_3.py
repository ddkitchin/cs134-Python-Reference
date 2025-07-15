#@copyright Deborah Kitchin
from random import randint

def main()-> None:
    # Tuple example DOES NOT CHANGE AFTER DEFINED May see this, but not expected to use.
    # noinspection SpellCheckingInspection
    roster_tuple = ("Debbie", "Nancy", "Amber", "Aricke", "Dylan", "Jeffery", "AJ")
    print(roster_tuple)

    store_sales = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # I have 10 store_s

    months = ["January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"]

    # I have a table of 10 store_s with sales for each of the 12 months.
    month_sales = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    print(store_sales)
    print(months)
    print(month_sales)
    store_total=0
    company_total=0
    for store in range(len(store_sales)):
        print("="*18,"Store",store_sales[store],"="*18)
        for month in range(len(months)):
            month_sales[store][month]=randint(0,100000)
            store_total=store_total+month_sales[store][month]
            print(f"\t\t\t{months[month]:10} {month_sales[store][month]:10}")
        print(f"\t\tStore Total {store_total:17}")
        company_total=company_total+store_total
        store_total=0
    print(f"\tCompany Total {company_total:23}")


if __name__ == "__main__":
    main()