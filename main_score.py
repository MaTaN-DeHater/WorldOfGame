from flask import Flask, render_template_string, redirect, url_for
import os
import json
from score import wipe_score

app = Flask(__name__)

SCORES_FILE_NAME = "scores.json"
BAD_RETURN_CODE = -1


def read_scores():
    if not os.path.exists(SCORES_FILE_NAME):
        return {}
    with open(SCORES_FILE_NAME, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


@app.route('/')
def score_server():
    try:
        scores = read_scores()
        if scores:
            score_text = ""
            for user, games in scores.items():
                score_text += f"User: {user}\n"
                for game, difficulties in games.items():
                    score_text += f"  Game: {game}\n"
                    for difficulty, score in difficulties.items():
                        score_text += f"    Difficulty {difficulty}: {score} Points\n"
        else:
            score_text = "No scores available."

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The scores are:</h1>
            <pre id="score">{score_text}</pre>
            <form action="/wipe" method="post">
                <button type="submit">Wipe Scores</button>
            </form>
        </body>
        </html>
        """
    except Exception as e:
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Scores Game</title>
        </head>
        <body>
            <h1>ERROR:</h1>
            <div id="score" style="color:red">{str(e)}</div>
        </body>
        </html>
        """

    return render_template_string(html_content)


@app.route('/wipe', methods=['POST'])
def wipe_score_route():
    try:
        wipe_score()
    except Exception as e:
        return f"An error occurred while wiping the score: {e}", BAD_RETURN_CODE
    return redirect(url_for('score_server'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8777)
