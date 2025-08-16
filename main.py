def get_book_txt(file_path):
    if type(file_path) is str:
        with open(file_path) as f:
            file_contents = f.read()
            return file_contents
    else:
        print("incorrect file path!")
        return None

def num_words_in_book(text):
    if type(text) is str:  
        words = text.split()
        word_count = len(words)
        return word_count
    else:
        print("num_words() incorrect type")
        return None


def main():
    book_file_path =  "books/frankenstein.txt"
    book_text = get_book_txt(book_file_path)
    book_word_count = num_words_in_book(book_text)
    print(f"{book_word_count} words found in the document")

main()
