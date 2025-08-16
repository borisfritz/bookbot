# Take in file_path as STRING and return file_contents as a STRING
    #if argument IS NOT a STRING return NONE and Print EnvironmentError

def get_book_txt(file_path):
    if type(file_path) is str:
        with open(file_path) as f:
            file_contents = f.read()
            return file_contents
    else:
        print("incorrect file path!")
        return None

# MAIN PROGRAM

def main():

    from stats import count_words
    from stats import count_letters

    # Import Book from file and store as a STRING
    book_file_path =  "books/frankenstein.txt"
    book_text = get_book_txt(book_file_path)

    # Find and print the book's word count
    book_word_count = count_words(book_text)
    print(f"{book_word_count} words found in the document")

    # print 'letter: count' for each letter
    book_letter_count = count_letters(book_text)
    print(book_letter_count)

main()
