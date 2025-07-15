## 
#  This program builds the index of a book from terms and page numbers.
#

def main() -> None:
    # Create an empty dictionary.
    index_entries = {}

    # Extract the data from the text file.
    infile = open("index_data.txt", "r")
    print(type(infile))
    fields = extract_record(infile)
    while len(fields) > 0:
        add_word(index_entries, fields[1], fields[0])
        fields = extract_record(infile)

    infile.close()

    # Print the index listing.
    print_index(index_entries)


## Extract a single record from the input file.
#  @param infile the input file object
#  @return a list containing the page number and term or an empty list if
#  the end of file was reached
#
def extract_record(infile) -> list:
    line = infile.readline()
    if line != "":
        fields = line.split(":")
        page = int(fields[0])
        term = fields[1].rstrip()
        return [page, term]
    else:
        return []

    ## Add a word and its page number to the index.


#  @param entries the dictionary of index entries
#  @param term the term to be added to the index
#  @param page the page number for this occurrence of the term
#
def add_word(entries: dict, term: str, page: int) -> None:
    # If the term is already in the dictionary, add the page to the set.
    if term in entries:
        page_set = entries[term]
        page_set.add(page)

    # Otherwise, create a new set that contains the page and add an entry.
    else:
        page_set = {page}
        entries[term] = page_set


## Print the index listing.
#  @param entries a dictionary containing the entries of the index
#
def print_index(entries: dict) -> None:
    for key in sorted(entries):
        print(key, end=" ")
        page_set = entries[key]
        first = True
        for page in sorted(page_set):
            if first:
                print(page, end="")
                first = False
            else:
                print(",", page, end="")

        print()


# Start the program.
if __name__ == "__main__":
    main()
