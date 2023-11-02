# Instructions
# I was reading this article by Tim Urban 
# - Your Life in Weeks and realised just how little time we actually have.

# Create a program using maths and f-Strings 
# that tells us how many weeks we have left, if we live until 90 years old.

# It will take your current age as the 
# input and output a message with our time left in this format:

# You have x weeks left.
# Where x is replaced with the actual 
# calculated number of weeks the input age has left until age 90.

# Warning your output should match the 
# Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 1768 weeks left.

############        Answer       ###########

# age = int(input())
# total_weeks = (90 - age) * 52
# # print("You have " + str(total_weeks) + " weeks left.")
# # you can also print as:
# print(f"You have {total_weeks} weeks left")

#######################################################

print(int(8 /3))
print(round(8 / 3))
print(round(8 /3, 2))   #round into 2 decimal places
print(8 // 3)   #floor division
print(type(8 // 3))     #<class 'int'>

# math it out itself
result = 4 / 2
result = result + 1

# short hand
result /= 2
result += 1

# f-string
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your heighy is {height}, you are winning is {isWinning}")

#Learned today:
# Primitive Data Types
# Type Error, Type Checking and Type Conversion
# Mathematical Operations in Python
# Number Manipulation and F string in Python
