# memory_game.py
import random


def generate_sequence(difficulty):
    """
    Generates a list of random numbers between 1 and 101 with length equal to difficulty.

    :param difficulty: Length of the sequence to be generated.
    :return: List of random numbers.
    """
    return [random.randint(1, 101) for _ in range(difficulty)]


def is_list_equal(list1, list2):
    """
    Compares two lists to check if they are identical.

    :param list1: First list.
    :param list2: Second list.
    :return: True if both lists are identical, False otherwise.
    """
    return list1 == list2


def play(difficulty, user_sequence):
    """
    Initiates the Memory Game.

    :param difficulty: The difficulty level which determines the length of the sequence.
    :param user_sequence: List of numbers input by the user.
    :return: True if the user wins, False if the user loses.
    """
    generated_sequence = generate_sequence(difficulty)
    print(f"Generated sequence: {generated_sequence}")  # This line is for testing; we'll display it on the UI
    if is_list_equal(generated_sequence, user_sequence):
        return True
    else:
        return False
