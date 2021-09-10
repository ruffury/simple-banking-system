from account import Account
from login import Login
from personal_cabinet import PersonalCabinet


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

    def option3(self):
        print('Bye')
        exit()