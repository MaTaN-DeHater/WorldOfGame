# guess_game.py
import random

def generate_number(difficulty):
    """
    Generates a random number based on the difficulty level.
    """
    return random.randint(0, difficulty)

def get_guess_from_user(difficulty):
    """
    Prompts the user to guess a number.
    """
    guess = int(input(f"Guess a number between 0 and {difficulty}: "))
    return guess

def compare_results(secret_number, user_guess):
    """
    Compares the secret number and the user's guess.
    """
    return secret_number == user_guess

def play(difficulty):
    """
    Plays the Guess Game.
    """
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    if compare_results(secret_number, user_guess):
        print("You won!")
        return True
    else:
        print(f"You lost! The correct number was {secret_number}.")
        return False
