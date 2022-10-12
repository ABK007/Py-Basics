from os import system #import os library for using functionto clear console after each bidder
from art import logo # Importing logo string from art.py file

bidders = {}       
bid_amount = []

print(logo) # printing logo

while True:
    name = input("What is your name? ")
    bid = int (input("What is you bid? "))
    
    # Adding names and bidding amount in dictionary
    bidders[name] = bid
    
    # Asking for more bidders
    otherBidder = input("Are there any other bidders (yes/no): ").lower()
    
    #If yes the loop will restart after clearing the console
    if otherBidder == "yes":
        system('cls')
        pass
    
    # if no the it will find the name and amount of the highest bidder and then exit the loop
    elif otherBidder == "no":
        for amount in bidders.values():
            bid_amount.append(amount) #Adding the values in a list
        
        max_bid = max(bid_amount)
        
        for highest_bidder in bidders:
            if bidders[highest_bidder] == max_bid: # looking for the name of highest bidder
                winner = highest_bidder
        
        print(f"The winner is {winner} with bidding amount {max_bid}$ ") #prints winner message
        
        break 
        
    
