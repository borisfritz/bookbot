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

# Take in data and print the data in a readable format

def print_data(file_path, word_count, letter_list):
    if (type(file_path) is str) and (type(word_count) is int) and (type(letter_list) is list):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for letter in letter_list:
            print(f"{letter["char"]}: {letter["num"]}")
        print("============= END ===============")
    else:
        print("Print Error")
        return None


# MAIN PROGRAM

def main():

    from stats import count_words
    from stats import count_letters
    from stats import sort_letters_by_count

    book_file_path =  "books/frankenstein.txt"
    book_text = get_book_txt(book_file_path)
    book_word_count = count_words(book_text)
    book_letter_count = count_letters(book_text)
    book_letters_sorted = sort_letters_by_count(book_letter_count)

    print_data(book_file_path, book_word_count, book_letters_sorted)

# Run Main Program
main()
