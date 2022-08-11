import re
from caesar_cipher.corpus_loader import word_list, name_list

def count_words(text):
    candidate_words = text.split()
    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
        else:
            pass

    return word_count

def check_confidence(text):
    words = count_words(text)
    percentage = int(words / len(text.split()) * 100)

    if percentage > 50:
        return True
    else:
        return False