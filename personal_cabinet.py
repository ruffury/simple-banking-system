from luhn import check_number

import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()


class PersonalCabinet:
    def __init__(self, card_id):
        self.card_id = card_id
        self.menu_options = {
            1: 'Balance',
            2: 'Add income',
            3: 'Do transfer',
            4: 'Close account',
            5: 'Log out',
            0: 'Exit'
        }

    # todo think about duplicated code
    def print_menu(self):
        for key in self.menu_options.keys():
            print(f'{key}. {self.menu_options[key]}')

    def get_balance(self):
        cur.execute(f'select balance from card where id = {self.card_id}')
        balance = cur.fetchone()[0]
        print('Balance:', balance)
        return balance

    def add_income(self):
        income = int(input('Enter income'))
        cur.execute(f'update card set balance = balance + {income} where id = {self.card_id}')
        conn.commit()
        print('Income was added!')

    def do_transfer(self):
        print('Transfer')
        receiver_num = input('Enter card number')
        cur.execute(f'select * from card where number = {receiver_num}')
        receiver = cur.fetchone()
        if not check_number(receiver_num):
            print('Probably you made a mistake in the card number. Please try again!')
            return
        elif not receiver:
            print('Such a card does not exist.')
            return
        elif receiver[0] == self.card_id:
            print('You can\'t transfer money to the same account!')
            return
        else:
            transfer_money = int(input('Enter how much money you want to transfer:'))
            if transfer_money > self.get_balance():
                print('Not enough money!')
                return
            else:
                cur.execute(f'update card set balance = balance + {transfer_money} where number = {receiver_num}')
                conn.commit()
                cur.execute(f'update card set balance = balance - {transfer_money} where id = {self.card_id}')
                conn.commit()
                print('Success!')
                return

    def close_account(self):
        cur.execute(f'delete from card where id = {self.card_id}')
        conn.commit()
        print('The account has been closed!')

    @staticmethod
    def log_out():
        print('You have successfully logged out!')

    @staticmethod
    def exit():
        print('Bye')
        exit()
