class Login:
    @staticmethod
    def check_creds(accounts):
        card_num = input('Enter your card number:')
        pin = input('Enter your PIN:')

        return {card_num: pin} in accounts
