import sys

maximum = - sys.maxsize
input_value = input('Write value ->')

for i in range(2):
    try:
        maximum = max(int(input_value), maximum)
        input_value = input('Write value ->')
    except ValueError:
        print('Not a number, can\'t calculate max from 3 numbers')


print('Maximum input value is', maximum)

# in case you want to make the program endless here is the cose sample that will work until input is not numeric value:
# import sys
#
# maximum = - sys.maxsize
# input_value = input('Write value ->')
# is_number = True
#
# while is_number:
#     try:
#         maximum = max(int(input_value), maximum)
#         input_value = input('Write value ->')
#     except ValueError:
#         is_number = False
#
# print('Maximum input value is', maximum)
