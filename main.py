from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    print(f"{get_word_count(get_book_text("./books/frankenstein.txt"))} words found in the document")
main()