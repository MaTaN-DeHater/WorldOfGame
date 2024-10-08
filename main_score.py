# main_score.py
import random

from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from score import load_scores, add_score
from memory_game import play as memory_play, generate_sequence
from guess_game import play as guess_play
from currency_roulette_game import play as currency_roulette_play, get_money_interval

app = Flask(__name__)

# Set the secret key for session management
app.secret_key = 'secret'  # Replace 'your_secret_key_here' with any random string or a secure value

# Global variable to store username during the session
username = ""


@app.route('/')
def home():
    """
    Home page for selecting a username and game.
    """
    return render_template('index.html')


@app.route('/set_username', methods=['POST'])
def set_username():
    """
    Set the username globally and redirect to the game selection page.
    """
    global username
    username = request.form.get('username')
    return redirect(url_for('select_game'))


@app.route('/select_game')
def select_game():
    """
    Page for selecting a game and difficulty level.
    """
    return render_template('select_game.html', username=username)


@app.route('/play_game', methods=['POST'])
def play_game():
    """
    Handles the form submission for game selection and redirects to the appropriate game route.
    """
    game_choice = request.form.get('game')
    difficulty = int(request.form.get('difficulty'))
    return redirect(url_for(game_choice, difficulty=difficulty))


@app.route('/memory_game/<int:difficulty>', methods=['GET', 'POST'])
def memory_game(difficulty):
    """
    Route for playing the Memory Game.
    """
    if request.method == 'POST':
        # Handle form submission and user input
        user_input = request.form.get('user_sequence').split()
        user_sequence = list(map(int, user_input))  # Convert input to list of integers
        # Retrieve generated sequence from the session
        generated_sequence = session.get('generated_sequence')

        # Compare user's sequence with generated sequence
        if memory_play(difficulty, user_sequence):
            add_score(username, 'memory_game', difficulty)
            result = f"Congratulations {username}, you won the Memory Game!"
        else:
            result = f"Sorry {username}, you lost the Memory Game. The correct sequence was {generated_sequence}."

        # Clear the session value for generated sequence after use
        session.pop('generated_sequence', None)
        return render_template('result.html', result=result)

    # Generate a new sequence for GET request and store it in the session
    generated_sequence = generate_sequence(difficulty)
    session['generated_sequence'] = generated_sequence  # Save the sequence in session for comparison

    # Render the memory game page and show the sequence
    return render_template('memory_game.html', difficulty=difficulty, sequence=generated_sequence)


@app.route('/guess_game/<int:difficulty>', methods=['GET', 'POST'])
def guess_game(difficulty):

    if request.method == 'POST':
        user_guess = int(request.form.get('user_guess'))
        if guess_play(difficulty):
            add_score(username, 'guess_game', difficulty)
            result = f"Congratulations {username}, you won the Guess Game!"
        else:
            result = f"Sorry {username}, you lost the Guess Game."
        return render_template('result.html', result=result)
    return render_template('guess_game.html', difficulty=difficulty)


@app.route('/currency_roulette/<int:difficulty>', methods=['GET', 'POST'])
def currency_roulette(difficulty):

    usd_amount = random.randint(1, 100)  # Generate a random USD amount

    if request.method == 'POST':
        user_guess = float(request.form.get('user_guess'))
        lower_bound, upper_bound = get_money_interval(difficulty, usd_amount)

        if lower_bound <= user_guess <= upper_bound:
            add_score(username, 'currency_roulette_game', difficulty)
            result = f"Congratulations {username}, you won the Currency Roulette Game!"
        else:
            result = f"Sorry {username}, you lost the Currency Roulette Game. The correct range was between {lower_bound:.2f} and {upper_bound:.2f}."

        return render_template('result.html', result=result)

    return render_template('currency_roulette.html', difficulty=difficulty, usd_amount=usd_amount)


@app.route('/scores')
def display_scores():
    """
    Displays the current scores for all players.
    """
    scores = load_scores()
    return render_template('scores.html', scores=scores)


if __name__ == '__main__':
    app.run(debug=True)
