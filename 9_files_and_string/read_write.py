# @copyright Deborah Kitchin

DEFAULT_INPUT_FILE="digital_dreams.txt"
DEFAULT_OUTPUT_FILE="output.txt"
DEFAULT_FINAL_FILE="final.txt"

def main() -> None:

    # open files
    input_filename = input(f"Enter the input file name: (default={DEFAULT_INPUT_FILE})")
    if input_filename == "":
        input_filename = DEFAULT_INPUT_FILE

    output_filename = input(f"Enter the output file name: (default={DEFAULT_OUTPUT_FILE})")
    if output_filename == "":
        output_filename = DEFAULT_OUTPUT_FILE

    # read file in, revese characers in each line
    input_object = open(input_filename)
    output_object = open(output_filename, 'w')

    input_contents = input_object.readlines() # one character at a time
    for line in input_contents:
        # strip the new line at the end, reverse, and new line to the end
        # the newline from the input line would be first character on the line causing extra lines
        output_object.write(line.rstrip('\n')[::-1]+'\n')

    input_object.close()
    output_object.close()

    # read the output file, revese characers in each line, and write final file.
    input_object = open(output_filename)
    output_object = open(DEFAULT_FINAL_FILE, 'w')

    input_contents = input_object.readlines()  # one character at a time
    for line in input_contents:
        output_object.write(line.rstrip('\n')[::-1]+'\n')

    input_object.close()
    output_object.close()


if __name__ == "__main__":
    main()
