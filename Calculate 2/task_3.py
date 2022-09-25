name = input("Type your name ->")

# remove spaces from the input name from start and end
first_name = name.strip()

if len(first_name) < 3:
    print("Yor name is to short, the minimum length is 3, your input is {} charters length".format(len(first_name)))
else:
    print("Second letter in your name is {}", first_name[1: 2])
    print("Second and third letters in your name are {}", first_name[1: 3])
