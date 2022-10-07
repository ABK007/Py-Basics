import random #imported random library

word_list = ["Hello", "good", "delicious"] #list of words for passing as argument in random_word_selection function

def random_word_selection(list):
    """ Returns a word randomly selected from the words list passed as argument for guessing """
    random_index = random.randrange(len(list))
    word = word_list[random_index]
    return word

def generate_blanks(word):
    """ Returns blanks according to the number of letters in a word """
    blanks = ""
    for i in range(len(word)):
        blanks += "_  "
    return blanks
