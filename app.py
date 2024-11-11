from score import add_score


def welcome():
    name = input("What is your name? ")
    print(f"Hi {name} and welcome to the World of Games: The Epic Journey")
    return name


def start_play(user):
    while True:
        game_option = None
        while game_option not in [1, 2, 3]:
            try:
                game_option = int(input("Please choose a game: \n"
                                        "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it "
                                        "back. \n"
                                        "2. Guess Game - guess a number and see if you chose like the computer.\n"
                                        "3. Currency Roulette - try and guess the value of a random amount of USD in ILS. \n"))
                if game_option not in [1, 2, 3]:
                    print("Invalid option. Please choose a valid game number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        difficulty_level = None
        while difficulty_level not in [1, 2, 3, 4, 5]:
            try:
                difficulty_level = int(input("Please choose a difficulty level between 1 and 5: "))
                if difficulty_level not in [1, 2, 3, 4, 5]:
                    print("Invalid difficulty level. Please choose a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        game_modules = {
            1: 'memory_game',
            2: 'guess_game',
            3: 'currency_roulette_game'
        }
        selected_game = game_modules[game_option]

        if selected_game == 'memory_game':
            from games.memory_game import play
        elif selected_game == 'guess_game':
            from games.guess_game import play
        elif selected_game == 'currency_roulette_game':
            from games.currency_roulette_game import play

        result = play(difficulty_level)
        print(f"Game result: {'Win' if result else 'Lose'}")

        if result:
            add_score(user, selected_game, difficulty_level)

        replay = input("Do you want to play another game? (yes/no): ").strip().lower()
        if replay != 'yes':
            break
