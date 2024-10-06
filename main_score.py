from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)


SCORES_FILE_NAME = "Scores.txt"

def read_score_from_file():

    try:

        if not os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'w') as file:
                file.write('0')


        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read().strip()

            if score.isdigit():
                return int(score)
            else:
                return 0
    except Exception as e:
        print(f"Error reading score file: {e}")
        return 0

@app.route('/')
def home():


    score = read_score_from_file()

    return render_template('score.html', SCORE=score)


@app.route('/get_score')
def get_score():
    score = read_score_from_file()
    return jsonify({'score': score})

if __name__ == '__main__':
    app.run(debug=True)
