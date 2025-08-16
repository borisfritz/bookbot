# Take in STRING text and return INT word_count
    # if argument text IS NOT a STRING return NONE and print an error

def count_words(text):
    if type(text) is str:  
        words = text.split()
        word_count = len(words)
        return word_count
    else:
        print("count_words() incorrect type")
        return None

# Take in STRING text and return a dictonary of letter -> ammount found in text
    #if argument text IS NOT a STRING, return none and print error

def count_letters(text):
    letter_count = {}
    if type(text) == str:
        lower_case_text = text.lower()
        for l in lower_case_text:
            if l in letter_count:
                letter_count[l] += 1
            else:
                letter_count[l] = 1
        return letter_count
    else:
        print("count_letters() incorrect type")
        return None

