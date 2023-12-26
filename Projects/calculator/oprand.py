#   add
def add(n, m):
    return n + m

#   subtract
def substract(n, m):
    return n - m

#   multiplication
def mult(n, m):
    return n * m

#   division
def div(n, m):
    return n / m

operations = {
    '+' : add,
    '-' : substract,
    '*' : mult,
    '/' : div
}