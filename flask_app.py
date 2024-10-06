# flask_app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route to display the UI
@app.route('/')
def home():
    return render_template('index.html')

# Route to start the game and display results
@app.route('/play', methods=['POST'])
def play():
    user_name = request.form['username']
    game_option = request.form['game_option']
    # Call your game logic here and get results
    result = f"Hello {user_name}, you chose to play {game_option}."
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
