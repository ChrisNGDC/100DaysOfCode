from replit import clear
import art


def highest_bidder(bid_records):
    highest_bid = 0
    winner_name = "None"
    for bidder in bid_records:
        current_bid = bid_records[bidder]
        if current_bid > highest_bid:
            highest_bid = current_bid
            winner_name = bidder
    return winner_name, highest_bid


print(art.logo)
print("Welcome to the secret auction program.")
bidders = {}
end_of_auction = False

while not end_of_auction:
    name = input("What is your name?\n")
    bid = int(input("What's your bid?\n$"))

    bidders[name] = bid

    next_person = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    while next_person not in ["yes", "no"]:
        print("Invalid option.")
        next_person = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if next_person == "no":
        end_of_auction = True
    clear()

winner = highest_bidder(bidders)
print(f"The winner is {winner[0]} with a bid of ${winner[1]}.")
