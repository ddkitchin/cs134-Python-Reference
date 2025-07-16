# @copyright Deborah Kitchin

DEFAULT_INPUT_FILE="digital_dreams.txt"

def main() -> None:

    filename = input(f"Enter file name: (default={DEFAULT_INPUT_FILE})")
    if filename == "":
        filename = DEFAULT_INPUT_FILE

    # 1) read
    #filein_object= open(filename)
    #filein_contents = filein_object.read() # one character at a time
    #print(filein_contents)

    # 2 readlines
    #filein_object= open(filename)
    #filein_contents = filein_object.readlines() # one character at a time
    #for line in filein_contents:
    #   print(line, end='')

    # 3) readline
    filein_object = open(filename)

    # print one line at a time
    one_line = filein_object.readline()
    print(one_line)
    another_line = filein_object.readline()

    #print the rest of the lines in the file
    print(another_line)
    for line in filein_object:
        print(line, end="")

    filein_object.close()

if __name__ == "__main__":
    main()
