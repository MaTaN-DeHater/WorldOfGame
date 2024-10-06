from forex_python.converter import CurrencyRates
import random


def get_money_interval(usd_amount: float, difficulty: int) -> tuple[float, float]:
    currency_rate = CurrencyRates()
    usd_to_ils_rate = currency_rate.get_rate('USD', 'ILS')

    ils_amount = usd_amount * usd_to_ils_rate

    allowed_difference = 10 - difficulty

    lower_bound = ils_amount - allowed_difference
    upper_bound = ils_amount + allowed_difference

    return lower_bound, upper_bound


def get_guess_from_user(usd_amount: float) -> float:
    while True:
        try:
            guess = float(input(f"Please guess the value of {usd_amount} USD in ILS: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def compare_results(lower_bound: float, upper_bound: float, user_guess: float) -> bool:
    return lower_bound <= user_guess <= upper_bound


def play(difficulty: int) -> bool:
    usd_amount = random.randint(1, 100)

    lower_bound, upper_bound = get_money_interval(usd_amount, difficulty)

    user_guess = get_guess_from_user(usd_amount)

    is_winner = compare_results(lower_bound, upper_bound, user_guess)

    if is_winner:
        print(f"Congratulations! Your guess of {user_guess} ILS is within the acceptable range.")
    else:
        print(
            f"Sorry, your guess of {user_guess} ILS is not within the acceptable range of {lower_bound} to {upper_bound} ILS.")

    return is_winner
