from Functions import get_middle, hypotenuse, cost_of_shipping

if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 3]

    print("get_middle(list) =", get_middle(list))

    print("max(list) =", max(list))

    print("============================================")

    '''a = int(input("Enter a = "))
    b = int(input("Enter b = "))

    print("hypotenuse(a, b) =", hypotenuse(a, b))

    print("============================================")'''

    n = int(input("Enter number of items = "))

    print(f"Your shipping cost: ${cost_of_shipping(n):.2f}")
