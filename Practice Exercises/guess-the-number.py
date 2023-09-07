print("Guess a Number Game v1")
print("Guess the secret number!\n")

secret_number = 7
user_number = int(input("Guess a number between 1 and 10: "))

while user_number != secret_number:
    if user_number < secret_number:
        print("Too low")
    else:
        print("Too high")

    user_number = int(input("Please try again: "))

print(f"\nYou guessed it! It was {secret_number}!")
