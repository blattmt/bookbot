from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {file}')
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(get_book_text(file))} total words")
    print("--------- Character Count -------")
    sorted_dict(char_count(get_book_text(file)))
    print("============= END ===============")

main()