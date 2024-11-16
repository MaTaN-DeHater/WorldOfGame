from score import add_score
from games.memory_game import play as memory_game
from games.guess_game import play as guess_game
from games.currency_roulette_game import play as currency_game


def welcome():
    name = input("What is your name? ")
    print(f"Hi {name} and welcome to the World of Games: The Epic Journey")
    return name


def start_play(user):
    while True:
        game_option = get_valid_input(
            "Please choose a game: \n"
            "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back. \n"
            "2. Guess Game - guess a number and see if you chose like the computer.\n"
            "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n",
            [1, 2, 3]
        )

        difficulty_level = get_valid_input(
            "Please choose a difficulty level between 1 and 5: ",
            [1, 2, 3, 4, 5]
        )

        games = {
            1: memory_game,
            2: guess_game,
            3: currency_game
        }
        selected_game = games[game_option]

        result = selected_game(difficulty_level)
        print(f"Game result: {'Win' if result else 'Lose'}")

        if result:
            add_score(user, selected_game.__name__, difficulty_level)

        replay = input("Do you want to play another game? (y/n): ").strip().lower()
        if replay not in ['y', 'yes']:
            break


def get_valid_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Invalid option. Please choose between {valid_range}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
