import random
import my_module    #a module form another file

# Any random integer from 1 - 10
random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)