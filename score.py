# score.py
import json
import os

SCORES_FILE_NAME = "scores.json"


def load_scores():
    """
    Loads scores from the JSON file. If the file does not exist, initializes an empty score dictionary.

    :return: A dictionary representing all scores.
    """
    # Check if the scores file exists, and create it if not
    if not os.path.exists(SCORES_FILE_NAME):
        # Create an empty score dictionary with the "players" key
        initial_scores = {"players": {}}
        save_scores(initial_scores)  # Save the initial structure to the file
        return initial_scores

    # Load the existing scores from the file
    with open(SCORES_FILE_NAME, "r") as file:
        return json.load(file)


def save_scores(scores):
    """
    Saves the given scores dictionary to the JSON file.

    :param scores: A dictionary containing the updated scores.
    """
    with open(SCORES_FILE_NAME, "w") as file:
        json.dump(scores, file, indent=4)


def add_score(username, game, difficulty):
    """
    Adds a score for a specific user, game, and difficulty.

    :param username: The name of the player.
    :param game: The type of game (e.g., "memory_game", "guess_game", "currency_roulette_game").
    :param difficulty: The difficulty level of the game (1 to 5).
    """
    scores = load_scores()  # Load the current scores from the JSON file

    # Set default values for nested dictionaries if keys are missing
    user_scores = scores["players"].setdefault(username, {})
    game_scores = user_scores.setdefault(game, {})

    # Calculate the new score
    points_of_winning = (difficulty * 3) + 5
    game_scores[difficulty] = game_scores.get(difficulty, 0) + points_of_winning

    save_scores(scores)  # Save the updated scores back to the JSON file
