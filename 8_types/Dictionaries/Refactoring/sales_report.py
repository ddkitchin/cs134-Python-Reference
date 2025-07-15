## 
#  This program processes a collection of sales data for flavors of ice cream
#  and prints a report sorted by flavor.
#

# Import a user-defined module that processes tabular data.
import tabular_data


def main() -> None:
    filename = input("Enter sales data file name: ")
    sales_data = tabular_data.read_data(filename)
    tabular_data.print_report(sales_data)


if __name__ == "__main__":
    main()
