def validate_ticket(number):
    number.replace('-', '')
    if (number.__sizeof__() != 8) & (not number.isnumeric()):
        raise RuntimeError('Invalid ticket number')


ticket = input('print your ticket number ->')
validate_ticket(ticket)
first_sum = 0
second_sum = 0
for i in range(0, 8):
    if i < 4:
        first_sum += int(ticket[i])
    else:
        second_sum += int(ticket[i])

if first_sum == second_sum:
    print("The ticket {} is lucky".format(ticket))
else:
    print("The ticket {} is not lucky".format(ticket))
