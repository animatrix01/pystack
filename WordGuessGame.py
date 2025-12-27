import random

easy_words = [
    "cat", "dog", "sun", "run", "eat", "fly", "big", "red", "blue", "car",
    "bus", "ten", "one", "two", "hat", "mat", "sit", "top", "hot", "ice",
    "ant", "bee", "cup", "pen", "key", "map", "leg", "arm", "eye", "day",
    "sky", "sea", "art", "war", "new", "old", "try", "use", "get", "set",
    "put", "cut", "wet", "dry", "sad", "bad", "fun", "why", "how", "who"
]

medium_words = [
    "boat", "bird", "fish", "jump", "stop", "play", "game", "ball", "park",
    "tree", "leaf", "good", "cool", "warm", "dark", "book", "read", "word",
    "like", "home", "moon", "star", "rain", "snow", "wind", "fire", "lava",
    "road", "path", "ship", "bike", "work", "code", "list", "test", "help",
    "food", "meat", "soup", "cake", "milk", "gold", "iron", "rock", "sand",
    "time", "year", "week", "door", "wall"
]

hard_words = [
    "apple", "house", "water", "mouse", "chair", "table", "earth", "world",
    "happy", "smile", "laugh", "green", "white", "sugar", "bread", "stone",
    "river", "ocean", "friend", "letter", "magic", "music", "hello", "great",
    "funny", "beach", "money", "power", "study", "write", "dance", "pizza",
    "party", "smart", "brain", "heart", "light", "night", "cloud", "storm",
    "space", "fruit", "plant", "train", "plane", "watch", "clock", "sound",
    "dream", "place", "story"
]

def get_secrect_word():
    
    print("------------WELCOME TO WORD GUESSING GAME----------------")
    print("Choose ypur difficulty level: \n 1. Easy(3 words) \n 2. Medium(4 words) \n 3. Hard(5 words)")
    while True:
        try:
            level = input("Enter your choice : ")
            if level == 1 or level == "easy":
                print("you choose easy")
                return random.choice(easy_words)
            elif level == 2 or level == "medium":
                print("you choose medium")
                return random.choice(medium_words)
            elif level == 3 or level == "hard":
                print("you choose hard")
                return random.choice(hard_words)
        except ValueError:
            print("invalid choice please enter valid choice ")
            
def play_game(secrect):
    attempts = 0
    print("\n Guess the secrect word")
    while True:
        guess = input("Enter your guess: ").lower()
        attempts += 1
        if guess == secrect:
            print(f'CONGRATULATIONS 🎉🎉. YOU GUESSED IT IN {attempts} ATTEMPTS')
            break
        
        hint = ""
        
        for i in range(len(secrect)):
            if i < len(secrect) and guess[i] == secrect[i]:
                hint += secrect[i]
            
            else:
                hint += " _ "
        
        print('HINT :' , hint )

def main():
    while True:
        word = get_secrect_word()
        play_game(word)
        
        play_again = input("\nPlay Again(y/n) : ").lower()
        if play_again != "y":
            print("Thanks for playing")
            break
        
if __name__ == "__main__":
    main()