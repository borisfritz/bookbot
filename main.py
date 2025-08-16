# Take in file_path as STRING and return file_contents as a STRING
    #if argument IS NOT a STRING return NONE and Print EnvironmentError
        # TODO: Add error handling

def get_book_txt(file_path):
    if type(file_path) is str:
        with open(file_path) as f:
            file_contents = f.read()
            return file_contents
    else:
        print("incorrect file path!")
        return None

def main():

    from stats import num_words_in_book

    book_file_path =  "books/frankenstein.txt"
    book_text = get_book_txt(book_file_path)
    book_word_count = num_words_in_book(book_text)
    print(f"{book_word_count} words found in the document")

main()
