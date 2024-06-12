import random

def guessing_game():
    print("Welcome to the Guessing Game..Verion-0.1 Developed by Lamar1!")
    print("I have chosen a number between 1 and 100.")
    print("Can you guess what it is?")

    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    guess = None
    attempts = 0

    # Game loop
    while guess != random_number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > random_number:
            print("Too high! Try again.")
        elif guess < random_number:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    guessing_game()
