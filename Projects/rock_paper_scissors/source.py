import rps_mod
import random

user = input("What do you choose? Type: 0 = Rock, 1 = Paper, 2 = Scissors\n")
r = random.randint(0, 2)
rock = rps_mod.rock
paper = rps_mod.paper
scissors = rps_mod.scissors
game = [rock, paper, scissors]

# player v. computer chose
print("You chose:\n")
print(game[user]())  # Invoke the function to print the choice
print("computer chose:\n")
print(game[r]())  # Invoke the function to print the choice

# rock
if game[r]() == game[user]():
    print(rps_mod.tie())
if game[user] == rps_mod.paper:
    print("You Lose")
if game[user] == rps_mod.scissors:
    print("You win")
    
# paper
# scissors
