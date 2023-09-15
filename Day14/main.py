import art
import data
import random
from replit import clear


def show_data(selection_data):
    return f" Name: {selection_data['name']}\n Description: {selection_data['description']}"


def has_more_followers(x, y):
    return x["follower_count"] >= y["follower_count"]


def compare(player_choice, choice_a, choice_b):
    return (player_choice == 'a' and has_more_followers(choice_a, choice_b)) or (player_choice == 'b' and has_more_followers(choice_b, choice_a))


print(art.logo)
game_over = False
score = 0
selection = random.sample(data.data, k=2)
a = selection[0]
b = selection[1]

while not game_over:
    print("A:" + show_data(a))
    print(art.vs)
    print("B:" + show_data(b))
    choice = input('Chose which has more more followers. Type "A" or "B" → ').lower()
    is_correct = compare(choice, a, b)
    if is_correct:

        score += 1
        print(f"Correct, current score: {score}")
        if choice == 'b':
            a = b
        b = a
        while b == a:
            b = random.choice(data.data)

    else:
        clear()
        print(art.logo)
        print("Wrong, Game Over.")
        print(f"Final Score: {score}")
        game_over = True
