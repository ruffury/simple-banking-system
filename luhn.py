def check_number(number):
    number = list(number)

    for i in range(1, len(number) + 1):
        if i % 2 != 0:
            number[i - 1] = str(int(number[i - 1]) * 2)

    for i, digit in enumerate(number):
        if int(digit) > 9:
            number[i] = str(int(number[i]) - 9)

    number_sum = sum([int(i) for i in number])
    return number_sum % 10 == 0