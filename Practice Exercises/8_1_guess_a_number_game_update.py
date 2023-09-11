# SETUP
import random

print("Guess a Number Game - New and Improved!")
print("Guess the secret number!\n")

# PROCESSING
play_again = True

while play_again:
    tries = 1
    number = random.randrange(10) + 1

    guess = int(input("\nGuess a number between 1 and 10: "))
    while True:
        if guess == number:
            break
        
        if 1 <= guess <= 10:
            if guess > number:
                print("Too high\n")
            else:
                print("Too low\n")
        else:
            print("The number is between 1 and 10.")
            
        guess = int(input("Guess a number between 1 and 10: \n"))
        tries += 1

    print("\nYou guessed it! It was", str(number) + "!")
    print("It only took you", str(tries) + " tries!\n")
    
    user_play_again = input("Play again? (Y or N): ")
    while user_play_again != "Y" and user_play_again != "N":
        user_play_again = input("Input not recognized. Please enter Y or N: ")

    if user_play_again == "Y":
        play_again = True
    else:
        play_again = False
