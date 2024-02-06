import random


def play_game():
    secret_number = random.randint(1, 10)
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 10. Can you guess it?")
    num_guesses = 0

    while True:
        guess = int(input("Enter your guess: "))
        num_guesses += 1
        if guess == secret_number:
            print("Correct! You guessed the number in", num_guesses, "guesses.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
play_game()