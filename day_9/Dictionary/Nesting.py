# Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# Nesting a List in a Dictionary
travel_log = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12},
    "A_Dictionary" : {"Within_Another_Dictionary" : ["Within(0)", "A(1)", "List(2)"], "Withing_Another_Dictionary2" : 2}
}

print(travel_log["A_Dictionary"])

# {
#     Key : Value(Key : Value_List[1, 2, 3], Key : Value(13)),
#     Key : Value(Key : Value_List[0, 1, 2], Key : Value(2))
# }

# Nesting a Dictionary in a List
travel_log = [
    {
        "country" : "France", 
        "cities_visited" : ["Paris", "Lille", "Dijon"], 
        "total_visits" : 12
    },
    {
        "KEY" : "VALUE", 
        "Within_Another_KEY" : ["Within(0)", "A(1)", "Value(2)"], 
        "Withing_Another_Key" : 2
    }
]