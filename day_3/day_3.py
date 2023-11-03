# if/else and conditional operations
# if condition:
#     do this
# else:
#     do this

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height? "))

# if height > 120:
#     print("You can ride the rollercoaster!!!!")
# else:
#     print("You're too short, dem cells weak ah hell")

# Odd or even

# number = int(input("Enter your favorite number!: "))
# if number % 2 == 0:
#     print("This is an Even number")
# else:
#     print("This is an Odd number")

#########   if/elif/else    ##########    
print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))

if height > 120:
    print("You can ride the rollercoaster!!!!")
    age = int(input("What is your age? "))
    
    if age >= 12:
        print("That'll be $12 for you today")
    elif age >= 8 and age < 12:
        print("That'll be $10 for you today")
    else:
        print("You get into the free for FREE!!!!!")
else:
    print("You're too short, dem cells weak ah hell")
    
    # logical Operations
    # and   - &&
    # or    - ||
    # not   - !()
    