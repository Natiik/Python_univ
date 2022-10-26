def avg(lst):
    return sum(lst) / len(lst)


lats = []
longs = []
inp = input("Print coordinates in format 'lat lon' ->")

i = 0

while not inp.__eq__("tuple"):
    inp_arr = inp.split(" ")

    if len(inp_arr) != 2:
        raise RuntimeError("invalid input")

    if inp_arr[0].isnumeric() & inp_arr[1].isnumeric():
        lats.insert(i, float(inp_arr[0]))
        longs.insert(i, float((inp_arr[1])))
        i = i + 1
    else:
        raise RuntimeError("invalid input")

    inp = input("Print coordinates in format 'lat lon' ->")

print("The output coordinates are: lat {}, lon {}".format(avg(lats), avg(longs)))
