import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Random Password Generator")
n_letters = int(input("How many letters would you like in your passowrd?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

password = ""

# Easy
for i in range(0, n_letters):
    password += random.choice(letters)
    
for i in range(0, n_symbols):
    password += random.choice(symbols)
    
for i in range(0, n_numbers):
    password += random.choice(symbols)
    
print(password)

# Hard
passwrd = []
h_pass = ""
size_of_list = n_letters + n_symbols + n_numbers
for i in range(0, n_letters):
    char = random.choice(letters)
    index = random.randint(0, size_of_list - 1)
    passwrd.insert(index, char)
    
for i in range(0, n_symbols):
    char = random.choice(symbols)
    index = random.randint(0, size_of_list - 1)
    passwrd.insert(index, char)

for i in range(0, n_numbers):
    char = random.choice(numbers)
    index = random.randint(0, size_of_list - 1)
    passwrd.insert(index, char)

for i in range(0, size_of_list):
    h_pass += passwrd[i]
    
print(h_pass)

# Alternative for hard part
password_list = []

for i in range(0, n_letters):
    password_list.append(random.choice(letters))    #   This is the same as
                                                    #           |
for i in range(0, n_symbols):                       #           |
    password_list += random.choice(symbols)         #       <----   this

for i in range(0, n_numbers):
    password_list.append(random.choice(symbols))

for i in range(0, size_of_list):
    h_pass += passwrd[i]
    
print(password_list)
random.shuffle(password_list)
print(password_list)

f_password = ""
for char in password_list:
    f_password += char

print(f"Your password is: {f_password}")