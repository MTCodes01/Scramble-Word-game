import random as r
#test
def guess(x):
    # Counter for the number of correct guesses
    n = 0
    # Read words from the file corresponding to the difficulty level
    with open(f"{x}.txt", 'r') as e:
        file = e.read().split(",")
    
    # Allow the player 5 attempts to guess words
    for i in range(5):
        lst = []
        # Choose a random word from the list
        word = r.choice(file).strip()
        
        # Convert the word into a list of letters
        for letter in word:
            lst.append(letter)
        
        # Shuffle the letters of the word
        for j in r.shuffle(lst):
            print(j, end='')
        
        # Ask the player for their guess
        if input("\nEnter Your Guess:") == word:
            print("Correct\n")
            n += 1
        else:
            print(f"Wrong, The answer was {word}\n")
    
    # Return the number of correct guesses
    return n

def Start(user):
    # Dictionary to store scores for different difficulty levels
    dict_ = {"Easy":0, "Medium":0, "Hard":0}
    print(f"\nWelcome, {user} to Word Guessing Game")
    
    while True:
        # Display menu for difficulty selection
        print("\nSelect your difficulty")
        print("1) Easy")
        print("2) Medium")
        print("3) Hard")
        print("4) Exit")
        
        # Get user's choice
        choice = input("Choose Your Option (1/2/3/4): ")
        
        # Process user's choice
        if choice == "1" or choice.lower() == "easy":
            dict_["Easy"] += guess("easy")
        elif choice == "2" or choice.lower() == "medium":
            dict_["Medium"] += guess("medium")
        elif choice == "3" or choice.lower() == "hard":
            dict_["Hard"] += guess("hard")
        elif choice == "4" or choice.lower() == "exit":
            # Display the final scoreboard and exit the game
            print("\nScoreboard\n")
            for i,j in dict_.items():
                if j != 0:
                    print(f"{i} : {j}")
            print("\nSuccessfully Exited!\n")
            quit()
        else:
            print("\nInvalid Choice")

# Main
Start(input("Enter your name:"))
