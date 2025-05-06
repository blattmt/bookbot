from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    file = "./books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {file}')
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(get_book_text(file))} total words")
    print("--------- Character Count -------")
    sorted_dict(char_count(get_book_text(file)))
    print("============= END ===============")

main()