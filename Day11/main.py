import random
import art
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(cards_list):
    if 10 in cards_list and 11 in cards_list:
        return 0
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def show_cards_hidden(user, computer):
    print(f'User Cards → {user} → {calculate_score(user)}')
    print(f'Computer Cards → [{computer[0]}, ?]')
    print('--------------------------------------')


def show_cards(user, computer):
    print(f'User Cards → {user} → {calculate_score(user)}')
    print(f'Computer Cards → {computer} → {calculate_score(computer)}')
    print('--------------------------------------')


def compare(user, computer):
    if computer == 0 or user > 21 or (0 < user < computer <= 21):
        print("Computer Wins")
    elif user == computer:
        print("Draw")
    else:
        print("User Wins")


end_program = "yes"
while end_program == "yes":
    clear()
    print(art.logo)
    end_of_game = False
    end_of_user_turn = False
    user_cards = []
    computer_cards = []

    user_cards.extend([deal_card(), deal_card()])
    computer_cards.extend([deal_card(), deal_card()])

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while not end_of_user_turn and not end_of_game:
        show_cards_hidden(user_cards, computer_cards)
        if user_score > 21 or 0 in [user_score, computer_score]:
            end_of_game = True
        else:
            response = input('Do you want another card? Type "yes" or "no.\n')
            if response == "yes":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                end_of_user_turn = True

    while computer_score < 17 and not end_of_game:
        show_cards(user_cards, computer_cards)
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    show_cards(user_cards, computer_cards)
    compare(user_score, computer_score)
    end_program = input('Do you wish to plat again? Type "yes" or "no.\n')
