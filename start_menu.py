from account import Account
from login import Login
from personal_cabinet import PersonalCabinet

import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS card 
(
    id INTEGER,
    "number" TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
);""")
conn.commit()


class StartMenu:
    def __init__(self):
        self.account_numbers = list()
        self.menu_options = {
            1: 'Create an account',
            2: 'Log into account',
            0: 'Exit'
        }

    def print_menu(self):
        for key in self.menu_options.keys():
            print(f'{key}. {self.menu_options[key]}')

    def option1(self):
        new_card = Account()

        # find last id in db
        cur.execute('select COALESCE(max(id), 0) + 1 from card')
        last_id = cur.fetchone()[0]

        # insert new account in db
        cur.execute(f"""
            INSERT INTO card
            (id, "number", pin, balance)
            VALUES({last_id}, {new_card.get_card_number()}, {new_card.get_pin()}, {new_card.get_balance()});
                     """)
        conn.commit()
        self.account_numbers.append({new_card.get_card_number(): new_card.get_pin()})
        print('Your card has been created')
        print('Your card number:')
        print(new_card.get_card_number())
        print('Your card PIN:')
        print(new_card.get_pin())

    def option2(self):
        log = Login()
        if log.check_creds(accounts=self.account_numbers):
            print('You have successfully logged in!')
            personal_cabinet = PersonalCabinet()
            while True:
                personal_cabinet.print_menu()
                option = int(input())
                if option == 1:
                    personal_cabinet.option1()
                elif option == 2:
                    personal_cabinet.option2()
                    return
                else:
                    personal_cabinet.option3()
        else:
            print('Wrong card number or PIN!')

    @staticmethod
    def option3():
        print('Bye')
        exit()
