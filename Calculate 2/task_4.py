array = ["122129", "jacob"]

for i in array:
    print("{} contains only numbers: {}".format(i, i.isdigit()))
    print("{} contains only letters: {}".format(i, i.isalpha()))
    print(i.capitalize())
    print("-------------------------------------------------->")
