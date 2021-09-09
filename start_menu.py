from account import Account


class StartMenu:
    account_numbers = list()

    menu_options = {
        1: 'Create an account',
        2: 'Log into account',
        0: 'Exit'
    }

    def print_menu(self):
        for key in self.menu_options.keys():
            print(f'{key}. {self.menu_options[key]}')

    def option1(self):
        new_card = Account()
        self.account_numbers.append(new_card.get_cheksum())
        print('Your card has been created')
        print('Your card number:')
        print(new_card.get_card_number())
        print('Your card PIN:')
        print(new_card.get_pin())

    def option2(self):
        pass

    def option3(self):
        pass