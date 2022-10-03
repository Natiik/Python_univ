x = float(input("print value for x ->"))
y = float(input("print value for y ->"))

if x > 0:
    if y > 0:
        print('dot is in 1st square')
    elif y == 0:
        print('dot is on axis x to the right from center')
    else:
        print('dot is in 4th square')
elif x < 0:
    if y > 0:
        print('dot is in 2nd square')
    elif y == 0:
        print('dot is on axis x to the left from center')
    else:
        print('dot is in 3th square')
else:
    if y > 0:
        print('dot is on axis y to the top from center')
    elif y == 0:
        print('dot is in the center')
    else:
        print('dot is on axis y to the bottom from center')
