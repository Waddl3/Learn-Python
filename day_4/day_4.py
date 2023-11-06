import random
# import my_module    #a module form another file

# Any random integer from 1 - 10
random_integer = random.randint(1, 10)
print(random_integer)

# print(my_module.pi)

#0.00000 - 0.99999...
random_float = random.random()

#0.0000... - 4.9999...
random_float = random.random() * 5

print(random_float)

love_score = random.randint(1, 100)
print(f"your love score is {love_score}")