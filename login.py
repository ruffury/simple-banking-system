import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()


class Login:
    @staticmethod
    def check_creds():
        card_num = input('Enter your card number:')
        pin = input('Enter your PIN:')

        cur.execute(f'select * from card where number = {card_num} and pin = {pin}')
        return cur.fetchone()
