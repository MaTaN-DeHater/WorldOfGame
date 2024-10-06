import random


def generate_number(difficulty: int) -> int:
    secret_number = random.randint(0, difficulty)
    return secret_number


def get_guess_from_user(difficulty: int) -> int:
    while True:
        try:
            user_guess = int(input(f"Please enter your guess (0 to {difficulty}): "))
            if 0 <= user_guess <= difficulty:
                return user_guess
            else:
                print(f"Invalid input. Please enter a number between 0 and {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def compare_results(secret_number: int, user_guess: int) -> bool:
    return secret_number == user_guess


def play(difficulty: int) -> bool:
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    is_winner = compare_results(secret_number, user_guess)
    if is_winner:
        print("Congratulations! You've guessed the correct number!")
    else:
        print(f"Sorry, you lost. The correct number was {secret_number}.")
    return is_winner
