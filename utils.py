import os

# Variables
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

# Functions
def screen_cleaner():
    # Clear the screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems (Linux, macOS, etc.)
        os.system('clear')