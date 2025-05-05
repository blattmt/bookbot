from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    file = "./books/frankenstein.txt"
    print(f"{get_word_count(get_book_text(file))} words found in the document")
    print(char_count(get_book_text(file)))

main()