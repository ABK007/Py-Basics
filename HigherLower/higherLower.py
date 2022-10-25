import random
from unicodedata import name
from game_data import data
from logos import logo
from logos import vs
from os import system



def select_option(data_list):
    """Returns a random dictionary from the data list"""    
    return random.choice(data_list)





def play_game():
    
    score = 0
    continue_game = True
    
    
    print (logo)
    
    option_a = select_option(data)
    option_b = select_option(data)
    
    while continue_game:
    
        option_a = option_b
        option_b = select_option(data)
        



        name_option_a = option_a['name']
        followers_option_a = option_a['follower_count']
        description_option_a = option_a['description']
        country_option_a = option_a['country']

        name_option_b = option_b['name']
        followers_option_b = option_b['follower_count']
        description_option_b = option_b['description']
        country_option_b = option_b['country']

        print(f"Compare A: {name_option_a}, {description_option_a}, {country_option_a}")

        print(vs)

        print(f"Against B: {name_option_b}, {description_option_b}, {country_option_b}")

        user_input = input("Who has more followers? Type 'A' or 'B':" )

        if user_input == "A":
            system('cls')
            
            if followers_option_a > followers_option_b:
                score += 1
                print (logo)
                print(f"You are right, your current score is {score}")
                
            else:
                print(logo)
                print(f"Sorry, that's wrong, your final score is: {score}")
                continue_game = False
                
        elif user_input == "B":
            system('cls')
            
            if followers_option_b > followers_option_a:
                score += 1
                print (logo)
                print(f"You are right, your current score is {score}")
            else:
                print(logo)
                print(f"Sorry, that's wrong, your final score is: {score}")
                continue_game = False

    
        
            
    
    
    
    
    
play_game()
    
    
    
    

    
    
    
      