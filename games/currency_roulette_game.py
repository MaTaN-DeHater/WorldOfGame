import random
import requests
from forex_python.converter import CurrencyRates


def get_money_interval(difficulty):
    c = CurrencyRates()
    try:
        exchange_rate = c.get_rate('USD', 'ILS')
    except Exception as e:
        print("Error fetching exchange rate. Please try again later.")
        return None, None

    usd_amount = random.randint(1, 100)

    ils_value = usd_amount * exchange_rate

    allowed_difference = 10 - difficulty

    interval = (ils_value - allowed_difference, ils_value + allowed_difference)

    return interval, usd_amount


def get_guess_from_user(usd_amount):
    while True:
        try:
            guess = float(input(f"Guess the ILS value for {usd_amount} USD: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def compare_results(interval, user_guess):
    return interval[0] <= user_guess <= interval[1]


def play(difficulty):
    interval, usd_amount = get_money_interval(difficulty)
    user_guess = get_guess_from_user(usd_amount)
    return compare_results(interval, user_guess)
