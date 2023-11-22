from ceaser_cipher import ceaser
from cc_logo import logo

#   Logo
print(logo)

active = True

while active:
    #   User text choice
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #   Encode or Decode
    ceaser(text, shift, direction)
    
    choice = input("End? 'n'; Otherwise: Press any key \n").lower()
    print("\n")
    if choice == "n": active = False