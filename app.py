def welcome():
    name = (input("What is your name? "))
    print(f"Hi {name} and welcome to the World of Games: The Epic Journey")


def start_play():
    game_option = input("Please choose a game: \n"
                        "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it "
                        "back. \n"
                        "2. Guess Game - guess a number and see if you chose like the computer.\n"
                        "3. Currency Roulette - try and guess the value of a random amount of USD in ILS. \n")
    # Validate the game option
    if game_option not in [1, 2, 3]:
        print("Invalid option. Please choose a valid game number.")
        return game_option

    # Prompt the user to select a difficulty level
    difficulty_level = input("Please choose a difficulty level between 1 and 5: ")

    # Validate the difficulty level
    if difficulty_level not in [1, 2, 3, 4, 5]:
        print("Invalid difficulty level. Please choose a number between 1 and 5.")
        return difficulty_level

    print(f"You have chosen game {game_option} with difficulty level {difficulty_level}.")
