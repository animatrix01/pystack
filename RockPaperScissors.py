# making rock paper scissors

import random

ROCK = "r"
SCISSOR = "s"
PAPER = "p"

emojis = {ROCK : "🪨" , SCISSOR : "✂️" , PAPER : "📃"}
choices = tuple(emojis.keys())
print(choices)

def get_user_choice():
    
    while True:
        user_choice = input("ROCK PAPER OR SCISSORS (r/p/s) : ").lower()
        if user_choice in choices:
            return user_choice
        
        else :
            print("Invalid choice")
            
def display_choice(user_choice , computer_choice):
    
    print(f"You chose {emojis[user_choice]}")
    print(f"computer chose {emojis[computer_choice]}")
    
def determine_winner(user_choice , computer_choice):
    
    if user_choice == computer_choice:
        print("TIE")
        
    elif(
        user_choice  == ROCK and computer_choice ==SCISSOR or 
        user_choice  == SCISSOR and computer_choice ==PAPER or
        user_choice  == PAPER and computer_choice ==ROCK):
        print("You won 🎉")
        
    else:
        print("you lose")
        
def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        
        display_choice(user_choice , computer_choice)
        determine_winner(user_choice, computer_choice)
        
        should_continue = input(" Wanna play again? (y/n) : ").lower()
        if should_continue == "n":
            print("thanks for playing")
            break
        
play_game()
    