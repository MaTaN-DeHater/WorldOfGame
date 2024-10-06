from guess_game import play as play_guess_game
from memory_game import play as play_memory_game
from currency_roulette_game import play as play_currency_roulette_game
from score import add_score
from utils import screen_cleaner


def welcome():
    name = input("What is your name? ")
    print(f"Hi {name} and welcome to the World of Games: The Epic Journey")


def start_play():
    screen_cleaner()

    game_option = input("Please choose a game: \n"
                        "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it "
                        "back. \n"
                        "2. Guess Game - guess a number and see if you chose like the computer.\n"
                        "3. Currency Roulette - try and guess the value of a random amount of USD in ILS. \n")

    try:
        game_option = int(game_option)
    except ValueError:
        print("Invalid input. Please enter a number corresponding to the game option.")
        return

    if game_option not in [1, 2, 3]:
        print("Invalid option. Please choose a valid game number.")
        return

    difficulty_level = input("Please choose a difficulty level between 1 and 5: ")

    try:
        difficulty_level = int(difficulty_level)
    except ValueError:
        print("Invalid input. Please enter a number for difficulty level.")
        return

    if difficulty_level not in [1, 2, 3, 4, 5]:
        print("Invalid difficulty level. Please choose a number between 1 and 5.")
        return

    print(f"You have chosen game {game_option} with difficulty level {difficulty_level}.")

    game_won = False

    if game_option == 1:
        game_won = play_memory_game(difficulty_level)
    elif game_option == 2:
        game_won = play_guess_game(difficulty_level)
    elif game_option == 3:
        game_won = play_currency_roulette_game(difficulty_level)

    if game_won:
        add_score(difficulty_level)
        print(f"Congratulations! You won the game. Your score has been updated.")
    else:
        print(f"Sorry, you lost the game. Better luck next time.")
