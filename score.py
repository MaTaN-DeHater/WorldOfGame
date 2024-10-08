# score.py

import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read())
        else:
            current_score = 0
    except (FileNotFoundError, ValueError):
        current_score = 0

    new_score = current_score + points_of_winning

    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))
    except IOError:
        return BAD_RETURN_CODE

    return new_score

def wipe_score():
    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write("0")
    except IOError:
        return BAD_RETURN_CODE

    return 0