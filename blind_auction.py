# I have simply uploaded an ASCI logo created in another file
from blind_auction_art import logo
print(logo)
# I have created an empty dictionary for our function later on, and the following boolean is for the while loop so that it doesn't exit the program after the first run
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # example dictionary :  bidding_record = {"Navid": 254, "Enzo": 360}
  # I created a for loop to iterate throough the keys within the dictionary
  # then created a variable bid_amount to store the values in, and finally an if statement to check which bid is actually higher
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  # The purpose of this input variable is to check whether to continue with the program or exit based on the user's decision
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    # this function is for clearing the IDE for the next series of input. You have to imoprt the the right package based on the IDE you are using
    clear()
  
