pro_dictionary = {"key" : "value"}

print(pro_dictionary["key"])

pro_dictionary["keys"] = "values"

print(pro_dictionary)

pro_dictionary[1] = 10

print(pro_dictionary)

#   create empty dictionary
empty = {}

# Wipe prog_dictionary
# pro_dictionary = {}
# print(pro_dictionary)

#   Edit iteam
pro_dictionary["keys"] = 100
print(pro_dictionary)

#   loop print
for item in pro_dictionary:
    print(item)    # only prints key
    print(pro_dictionary[item])     # only prints values