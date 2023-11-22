from alphabet import alphabet
    
def ceaser(text, shift, direction):
    ceaser_txt = ""
    size = len(alphabet)
    
    if direction == "decode":
            shift *= -1
    
    for c in text:
        if c  in alphabet:
            index = alphabet.index(c)
            new_index = index + shift
            if new_index >= size: new_index %= size
            ceaser_txt += alphabet[new_index]
        else:
            ceaser_txt += c

    print(f"The {direction} text is {ceaser_txt}")