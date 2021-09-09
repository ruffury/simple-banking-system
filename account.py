import random


class Account:
    def __init__(self):
        self.__bin = '400000'
        self.__account_number = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        self.__checksum = str(random.randint(0, 9))
        self.__card_number = self.__bin + self.__account_number + self.__checksum
        self.__pin = str(random.randint(0, 9999))

    def get_cheksum(self):
        return self.__checksum

    def get_card_number(self):
        return self.__card_number

    def get_pin(self):
        return self.__pin
