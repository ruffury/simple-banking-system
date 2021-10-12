import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()


class Account:
    def __init__(self):
        self.__bin = '400000'
        self.__account_number = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        self.__checksum = self.get_checksum(self.__bin + self.__account_number)
        self.__card_number = self.__bin + self.__account_number + self.__checksum
        self.__pin = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        self.__balance = 0

    @staticmethod
    def get_checksum(number):
        number = list(number)

        for i in range(1, len(number) + 1):
            if i % 2 != 0:
                number[i - 1] = str(int(number[i - 1]) * 2)

        for i, digit in enumerate(number):
            if int(digit) > 9:
                number[i] = str(int(number[i]) - 9)

        number_sum = sum([int(i) for i in number])
        if number_sum % 10 != 0:
            return str(10 - (number_sum % 10))
        else:
            return '0'

    def get_card_number(self):
        return self.__card_number

    def get_pin(self):
        return self.__pin

    def get_balance(self):
        return self.__balance
