import random


def generate_number(difficulty):
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f" Enter a number between 0 and {difficulty}: "))
            if 0 <= guess <= difficulty:
                return guess
            else:
                print(f"Please enter a number within the range 0 to {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def compare_results(secret_number, user_guess):
    return secret_number == user_guess


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, user_guess)
