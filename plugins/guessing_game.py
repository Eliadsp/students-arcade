import random

AUTHOR = "Eliad Spraggins"
APP_NAME = "Guessing Game"


def run():
    target = random.randint(1, 10)

    print("Guess a number from 1 to 10.")

    while True:
        response = input("Your guess: ")

        try:
            guess = int(response)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if guess < 1 or guess > 10:
            print("Please enter a number from 1 to 10.")
        elif guess < target:
            print("Too low. Try again.")
        elif guess > target:
            print("Too high. Try again.")
        else:
            return f"You guessed it! The number was {target}."