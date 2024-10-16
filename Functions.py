import math


def get_middle(list):
    return list[int(len(list) / 2)]


def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def cost_of_shipping(n):
    return 10.95 + (n-1) * 2.95

def is_prime(number):

    if number == 0 or number == 1:
        return False

    for i in range(2, int(number / 2 + 1)):
        if number % i == 0:
            return False
    return True
