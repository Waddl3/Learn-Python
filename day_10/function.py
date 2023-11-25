def format_name(f_name, l_name):
    # Base case
    if f_name == "" or l_name == "":  return
    name = f_name.title() + " " + l_name.title()
    return name

print(format_name("jesus", "rodriguez-luna"))

#   Note: title() makes each word titlecased

#Alternative

def format_name(f_name, l_name):
    name = f_name.title() + " " + l_name.title()
    return name

print(format_name(input("What is your first name? "),
                  input("What is your last name? ")))