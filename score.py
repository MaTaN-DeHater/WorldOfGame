import os
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE

POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5


def add_score(difficulty: int) -> None:
    points_to_add = POINTS_OF_WINNING(difficulty)

    try:

        if not os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'w') as file:
                file.write('0')

        # Read the current score
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = file.read().strip()
            if current_score.isdigit():
                current_score = int(current_score)
            else:
                current_score = 0

        new_score = current_score + points_to_add

        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))

        print(f"Score updated! Your current score is: {new_score}")

    except Exception as e:
        print(f"An error occurred while updating the score: {e}")
        return BAD_RETURN_CODE
