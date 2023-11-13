#Step 1 
import random
from hangman_fig import stages, logo
from hangman_words import word_list

def init_display(word):
    return ["_" for _ in range(len(word))]

chosen_word = random.choice(word_list)
display = init_display(chosen_word)
word_size = len(chosen_word)
letterUsed = []
end_game = False
lives = 6
    
#   Title Game Logo
print(logo)

while not end_game:
    guess = input("Guess a letter: ").lower()

    if guess in letterUsed:
        print(f"Letter: '{guess}' has already been used.\n")
    else:
        letterUsed.append(guess)
    
        for pos in range(word_size):
            char = chosen_word[pos]
            if char == guess:
                display[pos] = guess
                
        if guess not in display:
            lives -= 1
            if lives == 0:
                print(stages[lives] + "\nYou LOSE!!")
                break
        
        print(f"{' '.join(display)}")
        
        if "_" not in display:
            end_game = True
            print("You WIN!!")
        
        
        print(stages[lives])