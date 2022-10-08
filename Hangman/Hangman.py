import random #imported random library
from stages import stages
from stages import logo # Imported Hangman logo
from word_list import word_list #list of words for passing as argument in random_word_selection function

def random_word_selection(list):
    """ Returns a word randomly selected from the words list passed as argument for guessing """
    random_index = random.randrange(len(list))
    word = word_list[random_index]
    return word

def generate_blanks(word):
    """ Returns blanks according to the number of letters in a word """
    blanks = []
    for i in range(len(word)):
        blanks += "_"
    return blanks

def ask_letter():
    """ Asks the user input to type a letter and returns it as output """
    letter = input("Guess a letter: ")
    return letter

print(logo) #Prints hangman logo at the start of game
guess_word = random_word_selection(word_list) # Saves the randomly selected word

blanks = generate_blanks(guess_word) #Saves blanks in the form of list according to the length of word


Chances_left = 6 # Number of chances for player

while True:
    print(blanks)
    guessed_letter = ask_letter() # Stores letter typed by user

    if guessed_letter in guess_word:
# Below for loop iterates through guess_word and if letter is in the word, it replaces
# the blank in blanks list with the letter
        for index in range(len(guess_word)):
            if guessed_letter == guess_word[index]:
                blanks[index] = guessed_letter

    else:
# This piece of code decrease the number of chances in case of wrong letters
# And prints the string from stages list according to the chances left
        Chances_left = Chances_left - 1
        print(stages[Chances_left])
        if Chances_left == 0 : # Exits while loop when chances left are zero
            break


#Following code checks if there is no blank left in blanks list, then print message
#and  exit the while loop using break keyword.
    if "_" not in blanks:
        print("You have guessd the word correctly. You won.")
        break
