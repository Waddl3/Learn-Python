from alphabet import alphabet

# def encrypt(text, shift):
#     encrypted_text = ""
#     size = len(alphabet)
#     for c in text:
#         index = alphabet.index(c)
#         new_index = shift + index
#         if new_index >= size:
#             new_index %= size
#         encrypted_text += alphabet[new_index]
    
#     print(f"The encoded text is {encrypted_text}")
        
# def decode(text, shift):
#     decoded_txt = ""
#     for c in text:
#         index = alphabet.index(c)
#         new_index = index - shift
#         decoded_txt += alphabet[new_index]
        
#     print(f"The encoded text is {decoded_txt}")

#   Put everything into one single method.
    
def ceaser(text, shift, direction):
    ceaser_txt = ""
    size = len(alphabet)
    
    if direction == "decode":
            shift *= -1
    
    for c in text:
        if c == " " or c == ";":
            if c == " ":
                c 
            
        index = alphabet.index(c)
        new_index = index + shift
        if new_index >= size: new_index %= size
        ceaser_txt += alphabet[new_index]

    print(f"The {direction} text is {ceaser_txt}")
    
    # TO-DO: What is user enters a number/symbol/space?
    # TO-DO: Restart feature?
    # TO-DO: What is user enters shidt greater than 26