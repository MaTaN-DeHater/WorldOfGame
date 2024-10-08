from flask import Flask, render_template_string, redirect, url_for
import os
from score import wipe_score

app = Flask(__name__)

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

@app.route('/')
def score_server():
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                score = file.read()
        else:
            score = "0"
        html = f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is:</h1>
            <div id="score">{score}</div>
            <form action="/wipe" method="post">
                <button type="submit">Wipe Score</button>
            </form>
        </body>
        </html>
        """
    except Exception as e:
        html = f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>ERROR:</h1>
            <div id="score" style="color:red">{str(e)}</div>
        </body>
        </html>
        """
    return render_template_string(html)

@app.route('/wipe', methods=['POST'])
def wipe_score_route():
    wipe_score()
    return redirect(url_for('score_server'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)