def guessing(guess, user, computer):
    """Checking if user match, isHigher, isLower"""
    if user == computer:
        print("You guess the right answer! Congrats!")
        return -1, True
    elif user < computer:
        print("Too Low.\nGuess again")
        guess -= 1
    else:
        print("Too High.\nGuess again")
        guess -= 1
    return guess, False

def guessesLeft(guess):
    """Returns the number of turns remaining"""
    print(f"You have {guess} attempts remaining to guess the number.")
    return int(input("Make a guess: "))

def restart_game(game):
    """False to try again, True to end game"""
    if game == 'y':
        return False
    else:
        return True