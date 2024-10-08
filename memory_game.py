import random
import time
import utils


def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]


def get_list_from_user(difficulty):
    while True:
        try:
            user_input = input(f"Enter the {difficulty} numbers you remember, separated by spaces: ")
            user_sequence = list(map(int, user_input.split()))
            if len(user_sequence) == difficulty:
                return user_sequence
            else:
                print(f"Please enter exactly {difficulty} numbers.")
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")


def is_list_equal(generated_sequence, user_sequence):
    return generated_sequence == user_sequence


def play(difficulty):
    generated_sequence = generate_sequence(difficulty)
    print("Remember this sequence:")
    print(generated_sequence)
    time.sleep(0.7)
    utils.clear_console()
    user_sequence = get_list_from_user(difficulty)
    return is_list_equal(generated_sequence, user_sequence)
