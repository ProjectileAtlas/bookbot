from stats import numberofWords
from stats import charnumbers
from stats import dictPrint
import sys


def main():
    filepath=str
    dict = {}
    freq = {}
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath= sys.argv[1]
        print("File path:", filepath)
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print(get_book_text(filepath))
    word_count = numberofWords(filepath)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    chars = charnumbers(filepath)
    print(chars)
    print("============= END ===============")
    dictPrint()



def get_book_text(filepath):
    with open(filepath) as f:
        filecontent = f.read()
    return filecontent

main()


