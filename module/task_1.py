def is_phone_number_cool(phone_number):
    if len(phone_number) != 10 or not phone_number.isnumeric():
        raise RuntimeError('Wrong number')

    same_digit_count = 1
    for i in range(len(phone_number) - 1):
        if int(phone_number[i]) == int(phone_number[i + 1]):
            same_digit_count += 1
        else:
            same_digit_count = 1
        if same_digit_count >= 4:
            return True

    ascending_digit_count = 1
    for i in range(len(phone_number) - 1):
        if int(phone_number[i]) == int(phone_number[i + 1]) - 1:
            ascending_digit_count += 1
        else:
            ascending_digit_count = 1
        if ascending_digit_count >= 4:
            return True

    descending_digit_count = 1
    for i in range(len(phone_number) - 1):
        if int(phone_number[i]) == int(phone_number[i + 1]) + 1:
            descending_digit_count += 1
        else:
            descending_digit_count = 1
        if descending_digit_count >= 4:
            return True

    sum_first_digits = 0
    sum_last_digits = 0
    for i in range(5):
        sum_first_digits += int(phone_number[i])
    for i in range(5, 10):
        sum_last_digits += int(phone_number[i])
    if sum_first_digits == sum_last_digits:
        return True

    return False


if __name__ == '__main__':
    phone_numbers = [
        "0981177770",
        "0951234567",
        "0670171123",
        "lolkek",
        "1231231",
        "1111025213",
        "0246499851"
    ]

    for number in phone_numbers:
        try:
            is_cool = is_phone_number_cool(number)
            if is_cool:
                print("Number ", number, " is cool !!!")
            else:
                print("Number ", number, " is usual.")
        except RuntimeError:
            print("Wrong number:", number)
