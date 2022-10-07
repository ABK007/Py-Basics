import random #imported random library

word_list = ["Hello", "good", "delicious"] #list of words for passing as argument in random_word_selection function

def random_word_selection(list):
    """ Randomly selects a word from the words list passed as argument for guessing """
    random_index = random.randrange(len(word_list))
    word = word_list[random_index]
    return word


print (random_word_selection(word_list))
