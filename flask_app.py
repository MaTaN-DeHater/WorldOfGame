# flask_app.py
from flask import Flask, render_template, request, jsonify
import guess_game
import memory_game
import currency_roulette_game

app = Flask(__name__)

# Store the current game state in a global variable for simplicity
game_state = {"game": None, "difficulty": None}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    """Starts the game based on user selection and displays the input box."""
    data = request.json
    game_state["game"] = data['game_option']
    game_state["difficulty"] = int(data['difficulty'])
    return jsonify({"message": "Game started", "game": game_state["game"]})

@app.route('/play_game', methods=['POST'])
def play_game():
    """Plays the game based on user input and returns the result."""
    player_input = request.json['player_input']
    difficulty = game_state["difficulty"]
    game = game_state["game"]

    # Call the appropriate game logic
    if game == 'Guess Game':
        secret_number = guess_game.generate_number(difficulty)
        result = guess_game.compare_results(secret_number, int(player_input))
    elif game == 'Memory Game':
        # Demo sequence for simplicity, you can replace it with session-based memory logic
        sequence = memory_game.generate_sequence(difficulty)
        result = memory_game.is_list_equal(sequence, [int(i) for i in player_input.split()])
    elif game == 'Currency Roulette':
        usd_amount, lower_bound, upper_bound = currency_roulette_game.get_money_interval(difficulty)
        result = currency_roulette_game.compare_results((lower_bound, upper_bound), float(player_input))
    else:
        result = False

    return jsonify({"result": "You won!" if result else "You lost!"})

if __name__ == '__main__':
    app.run(debug=True)
