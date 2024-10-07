# utils.py
import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
