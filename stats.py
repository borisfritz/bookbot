# Take in STRING text and return INT word_count
    # if argument text IS NOT a STRING return NONE
        # TODO: add error handling

def num_words_in_book(text):
    if type(text) is str:  
        words = text.split()
        word_count = len(words)
        return word_count
    else:
        print("num_words() incorrect type")
        return None
