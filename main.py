from art import *
from game_data import data
import random


def compare(user_input, account_A, account_B):
    if account_A["follower_count"] > account_B["follower_count"]:
        if user_input == "a":
            return True
        else:
            return False
    else:
        if user_input == "b":
            return True
        else:
            return False


def choose_account():
    account = random.choice(data)
    return account


account_A = choose_account()
account_B = choose_account()
while account_B == account_A:
    account_B = choose_account()

is_game_over = False
user_score = 0

while not is_game_over:
    print(logo)
    print(
        f'Compare A: {account_A["name"]},a {account_A["description"]}, from {account_A["country"]}.{account_A["follower_count"]}')
    print(vs)
    print(
        f'Compare B: {account_B["name"]},a {account_B["description"]}, from {account_B["country"]}.{account_B["follower_count"]}')
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_correct = compare(user_input, account_A, account_B)
    if is_correct:
        user_score += 1
        account_A = account_B
        account_B = choose_account()
        for _ in range(50):
            print("\n")
        print(f"You are right! Current score: {user_score}")
    else:
        is_game_over = True

print(f"Sorry, that's wrong. Final score: {user_score}")
