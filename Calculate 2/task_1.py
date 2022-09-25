x = float(input("Print any number ->"))
a = float(input("Your order in the list ->"))
y1 = x ** 6 - 2 * pow(x, 4) + 4 * x + 7
y2 = 3 * pow(x, 6) - 2 * pow(x, 5) + 4 * pow(x, 4) + 7 * pow(x, 3) - 4 * x - 5
y3 = 2 * pow(x, 8) - 4 * pow(x, 6) - 34 * pow(x, 4) + x + 18
y4 = a * pow(x, 6) - 2 * pow(x, 5) + 4 * a * pow(x, 4 * a) + 7 * pow(x, 3) + pow(x, a) - 4 * x - a
print(
    "If x = {}, the result of \n  first math problem -> {}\n  second math problem -> {}\n  third math problem -> {} ".format(
        x, y1, y2, y3))
print("If x = {} and a = {}, then y = {}".format(x, a, y4))
