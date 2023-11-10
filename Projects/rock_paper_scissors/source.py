import rps_mod
import random

user = int(input("What do you choose? Type: 0 = Rock, 1 = Paper, 2 = Scissors\n"))
r = random.randint(0, 2)
game = [rps_mod.rock, rps_mod.paper, rps_mod.scissors]

# player v. computer chose
print("You chose:\n")
print(game[user])  # Invoke the function to print the choice
print("computer chose:\n")
print(game[r])  # Invoke the function to print the choice

# rock
if game[r] == rps_mod.rock:
    if game[r] == game[user]:
        print(rps_mod.tie)
    if game[user] == rps_mod.paper:
            print("You win")
    if game[user] == rps_mod.scissors:
            print("You lose")
    
# paper
if game[r] == rps_mod.paper:
    if game[r] == game[user]:
        print(rps_mod.tie)
    if game[user] == rps_mod.rock:
            print("You Lose")
    if game[user] == rps_mod.scissors:
            print("You win")
    
# scissors
if game[r] == rps_mod.scissors:
    if game[r] == game[user]:
        print(rps_mod.tie)
    if game[user] == rps_mod.paper:
            print("You Lose")
    if game[user] == rps_mod.rock:
            print("You win")

########################    To-Do   ########################
#
#   TO-DO:  Validation Check: Must be between 0 - 2
#   TO-DO:  Welcome Title
#   TO-DO:  "Try Again" feature
#
############################################################
