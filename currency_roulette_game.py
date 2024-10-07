# currency_roulette_game.py
import random
import requests


def get_money_interval(difficulty, usd_amount):
    """
    Retrieves the current USD to ILS exchange rate and calculates an interval for the correct answer based on difficulty.

    :param difficulty: Difficulty level which determines the range of the acceptable interval.
    :param usd_amount: The randomly generated amount of USD to convert.
    :return: A tuple (lower_bound, upper_bound) representing the acceptable range in ILS.
    """
    # Retrieve the current USD to ILS exchange rate using a free API
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        response.raise_for_status()
        exchange_rate = response.json()["rates"]["ILS"]
    except Exception as e:
        print("Error fetching exchange rate. Defaulting to 3.5 ILS per USD.")
        exchange_rate = 3.5  # Default value if the API request fails

    # Calculate the expected value in ILS and the acceptable interval
    expected_value = usd_amount * exchange_rate
    margin_of_error = 10 - difficulty  # The allowed margin decreases as difficulty increases
    lower_bound = expected_value - margin_of_error
    upper_bound = expected_value + margin_of_error

    return lower_bound, upper_bound


def get_guess_from_user(usd_amount):
    """
    Prompts the user to input a guess for the converted value of the specified USD amount in ILS.

    :param usd_amount: The amount of USD to be converted.
    :return: The user's guessed value in ILS.
    """
    guess = float(input(f"Guess the value of {usd_amount} USD in ILS: "))
    return guess


def play(difficulty):
    """
    Executes the Currency Roulette Game.

    :param difficulty: Difficulty level which determines the range of the acceptable interval.
    :return: True if the user wins, False if the user loses.
    """
    usd_amount = random.randint(1, 100)  # Generate a random USD amount between 1 and 100
    lower_bound, upper_bound = get_money_interval(difficulty, usd_amount)
    print(
        f"Guess the value of {usd_amount} USD in ILS. Your guess should be between {lower_bound:.2f} and {upper_bound:.2f}")

    user_guess = get_guess_from_user(usd_amount)

    if lower_bound <= user_guess <= upper_bound:
        print("Great! Your guess is within the acceptable range. You won!")
        return True
    else:
        print(
            f"Sorry, your guess is out of the acceptable range. The correct value was between {lower_bound:.2f} and {upper_bound:.2f}.")
        return False
