import os
import json

SCORES_FILE_NAME = "scores.json"
BAD_RETURN_CODE = -1


def add_score(user, game, difficulty):
    points_of_winning = (difficulty * 3) + 5
    scores = {}

    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as file:
            try:
                scores = json.load(file)
            except json.JSONDecodeError:
                scores = {}

    user_scores = scores.get(user, {})
    game_scores = user_scores.get(game, {})
    current_score = game_scores.get(str(difficulty), 0)

    new_score = current_score + points_of_winning
    game_scores[str(difficulty)] = new_score
    user_scores[game] = game_scores
    scores[user] = user_scores

    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            json.dump(scores, file)
    except IOError:
        return BAD_RETURN_CODE

    return new_score


def wipe_score():
    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            json.dump({}, file)
    except IOError:
        return BAD_RETURN_CODE

    return 0
