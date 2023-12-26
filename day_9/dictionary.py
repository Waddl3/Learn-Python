# pro_dictionary = {"key" : "value"}

# print(pro_dictionary["key"])

# pro_dictionary["keys"] = "values"

# print(pro_dictionary)

# pro_dictionary[1] = 10

# print(pro_dictionary)

# #   create empty dictionary
# empty = {}

# # Wipe prog_dictionary
# # pro_dictionary = {}
# # print(pro_dictionary)

# #   Edit iteam
# pro_dictionary["keys"] = 100
# print(pro_dictionary)

# #   loop print
# for item in pro_dictionary:
#     print(item)    # only prints key
#     print(pro_dictionary[item])     # only prints values
    
# #####################################

# #   Nesting
# capitals = {
#     "France" : "Paris",
#     "Germany" : "Berlin",
# }

# #   Nesting a List in Dictionary

# # Nesting Dictionary in a Dictionary
# travel_log = {
#     "France" : {
#         "cities_visited" : ["Paris", "Lille", "Dijon"], 
#         "total_visits" : 12
#         },
#     "Germany": {
#         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits" : 5
#         }
# }
# print(travel_log)
# # You can nest a list within a list but its not as good as this^^^

# # Nesting Dictionary in a List
# travel_log = [
#     {   "country" : "France",
#         "cities_visited" : ["Paris", "Lille", "Dijon"], 
#         "total_visits" : 12
#     },
#     {
#         "country" : "Germany",
#         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits" : 5
#     }
# ]

# print(travel_log)


country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(c, v, l):
  # create empty dictionary
  new_country = {}
  new_country["country"] = c
  new_country["visits"] = v
  new_country["cities"] = l
  travel_log.append(new_country)
  
# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")