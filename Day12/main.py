import art
import random
from replit import clear

end = False
while not end:
    clear()
    print(art.logo)

    game_over = False

    print("I'm thinking a number between 1 and 100.")
    computer_choice = random.randint(1, 100)
    difficulty = input('Pick a difficulty, type "easy" or "hard".\n').lower()
    difficulties = {
        "easy": 10,
        "hard": 5
    }
    attempts = difficulties[difficulty]
    print(f"DEBUG: {computer_choice}")
    while not game_over:
        player_guess = int(input("Pick a number between 1 and 100 → "))
        if player_guess > computer_choice:
            print("Too high")
            attempts -= 1
        elif player_guess < computer_choice:
            print("Too low")
            attempts -= 1
        else:
            print(f"Correct, the number was {computer_choice}")
            break
        print(f"Attempts remaining: {attempts}")
        if attempts == 0:
            print("You run out of turns, you lose.")
            game_over = True
    if input('Do you wish to play again? Type "yes" or "no".\n').lower() != "yes":
        end = True
