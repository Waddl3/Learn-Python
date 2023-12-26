from logo import logo
from oprand import operations

symbol = ""
# logo
print(logo)

#print operation symbols
for key in operations:
    symbol += key + " "

print(symbol)


n = int(input("What's the first numbers?: "))
m = int(input("What's the second numbers?: "))
s = operations[input("Choose a symbol: ")]
t = s(n, m)
print(t)
    
while True:
    next_input = input("Enter the next number (or 'q' to quit): ")
    
    if next_input.lower() == 'q':
        break
    
    if not next_input.isdigit():
        print("Invalid input. Enter a digit or 'q' to quit.")
        continue
    
    next_number = int(next_input)
    print(symbol)
    
    selected_symbol = input("Symbol: ")
    
    if selected_symbol not in operations:
        print("Invalid operation symbol selected.")
        continue
    
    operation = operations[selected_symbol]
    t = operation(t, next_number)
    print(t)


