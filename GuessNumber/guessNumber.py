import random
from os import system

from logo import logo


def generate_number():
    """Returns a random number between 0 and 100"""
    return random.randint(0, 100)

def select_difficulty(level_string):
    """Returns number of chances depending on the user selects easy or hard option"""
    if level_string == "easy":
        return 10
    elif level_string == "hard":
        return 5
    
def compare(guess_number, user_guess):
    if guess_number > user_guess and  guess_number - user_guess > 5:
        print("Too Low")
        
    elif guess_number > user_guess and guess_number - user_guess < 5 :
        print("Low but near")
    
    elif guess_number < user_guess and guess_number - user_guess < -5 :
        print("Too High")
    
    elif guess_number < user_guess and guess_number - user_guess > -5 :
        print("High but near")
        
    elif guess_number == user_guess and guess_number - user_guess == 0 :
        print(f"you have guessed correctly. The number is : {guess_number} ")
        
    else: 
        print("Enter a valid number")
    

def play_game():
    
    print(logo)
    
    print("Let's think of a number between 0 and 100")
    
    difficulty = input("Choose difficulty level. Type 'easy' or 'hard' : ").lower()
    
    chances = select_difficulty(difficulty)
    
    print(f"You have {chances} chances remaining to guess the number")
    
    guess_number = generate_number()

    
    for _ in range(chances):
        user_guess = int(input ("Make a guess: "))
        compare(guess_number, user_guess)
        chances = chances - 1
        
        if guess_number == user_guess:
            break
        else:
            print("Guess Again")
            print(f"You have {chances} attempts remaining to guess the number correctly")
            if chances == 0:
                print("You lost the game")
    
    
    play_again = input("Do you want to play again yes/no: ").lower()
    if play_again == "yes":
        system('cls')
        play_game()
    elif play_again == "no":
        pass        
    
    
    
    
        
play_game()   
    