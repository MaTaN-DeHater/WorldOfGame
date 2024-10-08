import os

# Variables
SCORES_FILE_NAME = "Scores.json"
BAD_RETURN_CODE = -1



def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems (Linux, macOS, etc.)
        os.system('clear')

# Use the function to clear the console
clear_console()