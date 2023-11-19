from ceaser_cipher import ceaser
from cc_logo import logo

#   Logo
print(logo)

#   User text choice
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#   Encode or Decode
ceaser(text, shift, direction)