# @copyright Deborah Kitchin
import csv

DEFAULT_INPUT_FILE = "video_games_fata.csv"
#DEFAULT_INPUT_FILE = "made_up_fields.csv"
DEFAULT_OUTPUT_FILE = "output.txt"

def main() -> None:

    input_filename = input(f"Enter the input file name: (default={DEFAULT_INPUT_FILE})")
    if input_filename == "":
        input_filename = DEFAULT_INPUT_FILE

    output_filename = input(f"Enter the output file name: (default={DEFAULT_OUTPUT_FILE})")
    if output_filename == "":
        output_filename = DEFAULT_OUTPUT_FILE

    # with read
    with open(input_filename, 'r') as csvfile:
        input_file = csv.reader(csvfile, delimiter=',')
        print(input_file)
        for line in input_file:
            #print list
            print(line)
            # print each field on the line
            #for field in line:
            #    print(field,end="")
            #print()


    """ With format print
    with open(input_filename, 'r') as csvfile:
        input_file = csv.reader(csvfile, delimiter=',')

        # enumerate(lines, 1) takes the lines list and returns pairs of (index, item)
        # The 1 argument tells enumerate to start counting from 1 instead of the default 0
        # i gets the line number (1, 2, 3, etc.)
        # line gets the actual content of each line

        # go through each line
        for i, fields in enumerate(input_file, 1):
            # Remove newline, split by comma, align each field to 20 chars
            #fields = fields.strip().split(',')
            formatted_line = ''
            # go through each field
            for j, field in enumerate(fields):
                # no tab before first field
                if j > 0:
                    formatted_line += '\t'
                # left justify each field and takes up 20 characters
                formatted_line += field.ljust(20)
            print(formatted_line)"""

    '''# write items to a file
    row1 = ['100', '50', '29']
    row2 = ['76', '32', '330']

    with open(output_filename, 'w', newline='') as csvfile:
        grades_writer = csv.writer(csvfile)
        grades_writer.writerow(row1)
        grades_writer.writerows([row1, row2])'''


if __name__ == "__main__":
    main()
