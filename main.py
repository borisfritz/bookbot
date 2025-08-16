def get_book_text(file_path):
    if type(file_path) is str:
        with open(file_path) as f:
            file_contents = f.read()
            return file_contents
    else:
        print("incorrect file path!")
        return None

def main():
    book_file_path =  "books/frankenstein.txt"
    book_text = get_book_text(book_file_path)
    print(book_text)

main()
