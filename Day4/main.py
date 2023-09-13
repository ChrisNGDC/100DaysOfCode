import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n→ "))
if user_choice > 2:
    print("Invalid number. Closing game")
else:
    computer_choice = random.randint(0, 2)

    print(f"Your choice: {choices[user_choice]}")
    print(f"Computer choice: {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("Draw")
    elif (user_choice - computer_choice == 1) or (user_choice - computer_choice == -2):
        print("You win")
    else:
        print("You lose")
