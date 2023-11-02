#if the bill $150.00, spliut between 5 people, with 12% tip.
# each person should pay (amount / n people) * 1.12(tip)
#Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
amount = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? "))
n = int(input("How many people to split the bill? "))

total = (((tip / 100) * amount) + amount) / n
# print("Each person should pay: " + str(round(total, 2)))
# If we wanted to utilize the f-string, we'd do the following:
total = str(round(total, 2))
print(f"Each person should pay: {total}")

############    NOTE    ############
#   total = str(round((((tip / 100) * amount) + amount) / n), 2)
#   this DOES NOT WORK.
#
# #   Error message:
# total = str(round((((tip / 100) * amount) + amount) / n), 2)
#             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: str() argument 'encoding' must be str, not int
####################################
