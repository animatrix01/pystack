# making gueesing game 

import random
def restart_game():
    
    restart = input("Do you want to play again(y/n) : ").lower()
    
    if restart == 'y':
        print('Here we go again🔁')
        return True
    elif restart == 'n':
        print('thanks for playing😊')
        return False
    

def guessing_game():
    
    ans = random.randint(1,100)
    attempts = 0

    while True:
        try:
            guess =  int(input("Guess the Number : "))
            attempts += 1
            
            if guess<1 or guess>100:
                print('Please chose valid number')
                continue
            
            elif guess > ans:
                print("Too High")
                
            elif guess < ans:
                print("Too Low")
                
            else:
                if attempts == 1:
                    print('HAWEYES!🎯🎯, UNBLIEVEABLE YOU GUESSED IT IN 1 TRY')
                else:
                    print("CONGRATULATIONS! you guessed it correct in ",attempts)
                if restart_game():
                    return True
                else:
                    return False
                
        except ValueError:
            print("enter a valid number")

while True:
    if not guessing_game():
        break