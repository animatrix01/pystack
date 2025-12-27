import random

while True:
    
   choice = input("ROLL A DICE (y/n) : ").lower()
   if choice == "y":
       die1 = random.randint(1,6)
       die2 = random.randint(1,6)
       print(f"{die1},{die2}")
   elif choice == "n":
       print("THANK YOU FOR PLAYING")
       break
   else:
       print("INVALID CHOICE!")
 