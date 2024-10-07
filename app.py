# app.py
from score import add_score

# Global variable to store username across functions
username = ""

def welcome():
    """
    Prints a welcome message to the user.
    """
    global username
    username = input("Please enter your name: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey!")

def start_play():
    """
    Prompts the user to choose a game and difficulty level.
    """
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess Game - guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    game_choice = int(input("Enter the game number: "))
    difficulty = int(input("Please choose game difficulty from 1 to 5: "))

    # Determine the game and play
    game_map = {1: "memory_game", 2: "guess_game", 3: "currency_roulette_game"}
    game_name = game_map.get(game_choice)
    if not game_name:
        print("Invalid choice. Please restart the program.")
        return

    # Import the appropriate game module and start the game
    if game_choice == 1:
        from memory_game import play
    elif game_choice == 2:
        from guess_game import play
    elif game_choice == 3:
        from currency_roulette_game import play

    # Play the game and update score if user wins
    if play(difficulty):
        add_score(username, game_name, difficulty)
        print("Your score has been updated!")
    else:
        print("Better luck next time!")
