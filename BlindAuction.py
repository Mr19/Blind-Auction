from os import system, name
from art import logo


def clear():
    # cls for windows, posix for mac or linux
    system('cls') if name == 'nt' else system('clear')


def main():
    print(logo)
    print("Welcome to the secret auction program.")
    silent_auction_data = {}
    bidding_in_progress = True
    while bidding_in_progress:
        bidder_name = input("What is your Name: ")
        bidder_value = int(input("What's your bid: $"))
        silent_auction_data[bidder_name] = bidder_value
        continue_auction = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if continue_auction == "yes":
            clear()
        elif continue_auction == "no":
            clear()
            winner_name = ""
            winning_bid = 0
            for key, value in silent_auction_data.items():
                if value > winning_bid:
                    winner_name = key
                    winning_bid = value
            print(f"The winner is {winner_name} with a bid of ${winning_bid}.")
            bidding_in_progress = False


if __name__ == '__main__':
    main()

