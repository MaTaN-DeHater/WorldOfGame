import random
import requests



FIXED_EXCHANGE_RATE = 3.5

def get_money_interval(difficulty):
    usd_amount = random.randint(1, 100)
    ils_value = usd_amount * FIXED_EXCHANGE_RATE
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
