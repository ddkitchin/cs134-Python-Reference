##
#  This module provides functions for working with tabular data 
#  consisting of lists of numbers, each of which has a name.
#

## Reads the tabular data.
#  @param filename name of the input file
#  @return a dictionary with the keys and data lists found in the file
#
def read_data(filename: str) -> dict:
    # Create an empty dictionary.
    data = {}

    infile = open(filename, "r")

    # Read each record from the file.
    for line in infile:
        fields = line.split(":")
        key = fields[0]
        data[key] = build_list(fields)

    infile.close()
    return data


## Builds a list of values contained in the fields split from a string.
#  @param fields a list of strings comprising the record fields
#  @return a list of floating-point values
#
def build_list(fields: list) -> list:
    values = []
    for i in range(1, len(fields)):
        sales = float(fields[i])
        values.append(sales)

    return values


## Prints a sales report.
#  @param data a table composed of a dictionary whose values are lists of numbers
#
def print_report(data: dict) -> None:
    # Find the number of columns as the length of the longest list.
    number_of_columns = 0
    for row in data.values():
        if len(row) > number_of_columns:
            number_of_columns = len(row)

    # Create a list of column totals.
    column_totals = [0.0] * number_of_columns

    # Print the key sales.
    for key in sorted(data):
        print("%-20s" % key, end="")

        key_total = 0.0
        values = data[key]
        for i in range(len(values)):
            value = values[i]
            key_total = key_total + value
            column_totals[i] = column_totals[i] + value
            print("%10.2f" % value, end="")

        print(" " * 10 * (number_of_columns - len(values)), end="")
        print("%15.2f" % key_total)

    # Print the column totals.
    print("%20s" % " ", end="")
    for i in range(number_of_columns):
        print("%10.2f" % column_totals[i], end="")
    print()
