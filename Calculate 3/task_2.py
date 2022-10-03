import sys

maximum = - sys.maxsize
is_error = False

for i in range(3):
    try:
        input_value = input('Write value ->')
        maximum = max(int(input_value), maximum)
    except ValueError:
        is_error = True
        print('Not a number, can\'t calculate max from 3 numbers')
        break

if not is_error:
    print('Maximum input value is', maximum)

# in case you want to make the program endless here is the cose sample that will work until input is not numeric value:
# import sys
#
# maximum = - sys.maxsize
# is_number = True
#
# while is_number:
#     try:
#         input_value = input('Write value ->')
#         maximum = max(int(input_value), maximum)
#     except ValueError:
#         is_number = False
#
# print('Maximum input value is', maximum)
