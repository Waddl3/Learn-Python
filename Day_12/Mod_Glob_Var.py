enemies = 1

def increase_enemies():
    # global enemies  # takes the global enemies into the function
    # enemies += 1
    print(f"enemies inside function: {enemies}")
    # NOTE: you do NOT want to modify the global scope within the function
    # It will cause failures
    # Instead, we can return enemies as the output
    return enemies + 1
    
increase_enemies()
print(f"enemies outside function: {increase_enemies()}")