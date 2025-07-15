##
#  This program checks which words in a file are not present in a list of
#  correctly spelled words.
#

# Import the split function from the regular expression module.
from re import split


def main() -> None:
    # Read the word list and the document.
    correctly_spelled_words = read_words("words.txt")
    document_words = read_words("alice30.txt")

    # Print all words that are in the document but not the word list.
    misspellings = document_words.difference(correctly_spelled_words)
    for word in sorted(misspellings):
        print(word)


## Reads all words from a file.
#  @param filename the name of the file
#  @return a set with all lowercased words in the file. Here, a word is a 
#  sequence of upper- and lowercase letters
#   
def read_words(filename: str) -> set:
    word_set = set()
    input_file = open(filename, "r")

    for line in input_file:
        line = line.strip()
        # Use any character other than a-z or A-Z as word delimiters. The part inside [] is a regular expression.
        parts = split("[^a-zA-Z]+", line)
        for word in parts:
            if len(word) > 0:
                word_set.add(word.lower())

    input_file.close()
    return word_set


# Start the program.
if __name__ == "__main__":
    main()
