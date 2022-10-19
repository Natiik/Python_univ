input_str = "julia julia lex julia lex sara sara julia lex julia alex alina julia sara"

array = input_str.replace(" ", ",").split(",")
new_str = ""
julia_n = 0
for i in array:
    if i.__eq__('julia'):
        julia_n += 1
    if i.__eq__('lex'):
        new_str += " mark"
    elif i.__eq__('sara'):
        continue
    else:
        suffix = ' ' + i
        new_str += suffix

print("Number of words: {}".format(len(array)))
print("Number of julia : {}".format(julia_n))
print("New string after changes {}".format(new_str))
