
def process_item(x):
    y = x+1
    while not prime(y):
        y = y+1
    return y

def prime(x):
    if x<2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True
