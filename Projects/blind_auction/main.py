from logo import logo

# variable
name = ""
bid = 0
other = ""
bid_finished = False
bid_list = {}

# logo w/ welcome message
print(logo)
print("Welcome to the secret auction program.")

while not bid_finished:
    #   Ask user input
    name = input("What is your name?: ")   # value
    bid = int(input("WHat's your bid?: $"))   # key
    bid_list[bid] = name
    
    #   other bidders?
    other = input("Are there any other bidders? Y/N\n").lower()
    if other == 'n': bid_finished = True
    
h = max(bid_list)
print(f"Highest bid was ${h} from {bid_list[h]}")

# Note:     I'm aware that if I added more features like to check how much
# so and so put, this dictionary wouldn't be good. However, the task was
# supposed to get the users, and get the higher bidder as the winner.

# The worst-case complexity as O(n) and the best-case complexity as O(1)