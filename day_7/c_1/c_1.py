#Step 1 
import random
import hangman_fig

word_list = ["aardvark", "baboon", "camel"]
display = []
chosen_word = random.choice(word_list)
word_size = len(chosen_word)
end_game = False

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

for _ in range(word_size):
    display.append("_")



while not end_game:
    guess = input("Guess a letter: ").lower()

    for pos in range(word_size):
        char = chosen_word[pos]
        if char == guess:
            display[pos] = guess
            
        #   TODO-2: - If guess is not a letter in the chosen_word,
        #   Then reduce 'lives' by 1. 
        #   If lives goes down to 0 then the game should stop and it should print "You lose."

    print(display)
    if "_" not in display:
        end_game = True
        print("You WIN!!")