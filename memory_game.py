# memory_game.py

import random
import time


def generate_sequence(difficulty: int) -> list[int]:
    return [random.randint(1, 101) for _ in range(difficulty)]


def display_sequence(sequence: list[int], display_time: float = 0.7):
    print(f"Memorize this sequence: {sequence}")
    time.sleep(display_time)

    print("\n" * 100)


def get_list_from_user(difficulty: int) -> list[int]:
    user_input = input(f"Enter the {difficulty} numbers you saw, separated by space: ")
    try:

        user_numbers = list(map(int, user_input.split()))
        if len(user_numbers) == difficulty:
            return user_numbers
        else:
            print(f"Invalid input. You must enter exactly {difficulty} numbers.")
            return get_list_from_user(difficulty)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return get_list_from_user(difficulty)


def is_list_equal(sequence: list[int], user_sequence: list[int]) -> bool:
    return sequence == user_sequence


def play(difficulty: int) -> bool:
    sequence = generate_sequence(difficulty)

    display_sequence(sequence)

    user_sequence = get_list_from_user(difficulty)

    if is_list_equal(sequence, user_sequence):
        print("Congratulations! You have a great memory!")
        return True
    else:
        print(f"Sorry, the correct sequence was: {sequence}")
        return False
