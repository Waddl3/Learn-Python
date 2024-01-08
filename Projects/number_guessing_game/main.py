from logo import logo
import random
from guess import guessing, guessesLeft, restart_game

EASY = 10
HARD = 5

# Title
print(logo)

# Random Choice
computer_choice = random.randint(1, 100)
game_over = False

while not game_over:
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if (difficulty == 'easy'):
        guess = EASY
        while guess > 0:
            user = guessesLeft(guess=guess)
            guess, game_over = guessing(guess=guess, user=user, computer=computer_choice)
    else:
        guess = HARD
        while guess > 0:
            user = guessesLeft(guess=guess)
            guess, game_over = guessing(guess=guess, user=user, computer=computer_choice)
    
    if guess == 0:
            print("You've run out of guesses, you lose.")
            game_over = True
    game_over = restart_game(input("Play Again? ('y' or 'n'): "))
    