## 
#  This program processes a collection of sales data for flavors of ice cream
#  and prints a report sorted by flavor.
#

def main() -> None:
    sales_data = read_data("ice_cream.txt")
    print_report(sales_data)


## Reads the tabular data.
#  @param filename name of the input file
#  @return a dictionary whose keys are ice cream flavors and 
#  whose values are sales data
#
def read_data(filename: str) -> dict:
    # Create an empty dictionary.
    sales_data = {}

    infile = open(filename, "r")

    # Read each record from the file.
    for line in infile:
        fields = line.split(":")
        flavor = fields[0]
        sales_data[flavor] = build_list(fields)

    infile.close()
    return sales_data


## Builds a list of store sales contained in the fields split from a string.
#  @param fields a list of strings comprising the record fields
#  @return a list of floating-point values
#
def build_list(fields: list) -> list:
    store_sales = []
    for i in range(1, len(fields)):
        sales = float(fields[i])
        store_sales.append(sales)

    return store_sales


## Prints a sales report.
#  @param sales_data a table composed of a dictionary of lists
#
def print_report(sales_data: dict) -> None:
    # Find the number of stores as the length of the longest store sales list.
    number_of_stores = 0
    for store_sales in sales_data.values():
        if len(store_sales) > number_of_stores:
            number_of_stores = len(store_sales)

    # Create a list of store totals.
    store_totals = [0.0] * number_of_stores

    # Print the flavor sales.
    for flavor in sorted(sales_data):
        print("%-15s" % flavor, end="")

        flavor_total = 0.0
        store_sales = sales_data[flavor]
        for i in range(len(store_sales)):
            sales = store_sales[i]
            flavor_total = flavor_total + sales
            store_totals[i] = store_totals[i] + sales
            print("%10.2f" % sales, end="")

        print("%15.2f" % flavor_total)

    # Print the store totals.
    print("%15s" % " ", end="")
    for i in range(number_of_stores):
        print("%10.2f" % store_totals[i], end="")
    print()


# Start the program.
if __name__ == "__main__":
    main()
