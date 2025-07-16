# @copyright Deborah Kitchin

DEFAULT_OUTPUT_FILE="output.txt"

def main() -> None:

    output_filename = input(f"Enter the output file name: (default={DEFAULT_OUTPUT_FILE})")
    if output_filename == "":
        output_filename = DEFAULT_OUTPUT_FILE

    # 1) write to a file
    fileout_object = open(output_filename, 'w')

    fileout_object.write('what to write\n')
    fileout_object.write('You can keep writing.\n')
    fileout_object.write(f'str(10)\n')
    fileout_object.close()

    # 2 append to a file
    fileout_object = open(output_filename, 'a')
    fileout_object.write('new stuff to add')
    fileout_object.close()


if __name__ == "__main__":
    main()
