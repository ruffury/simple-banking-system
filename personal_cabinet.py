class PersonalCabinet:
    def __init__(self):
        self.balance = 0

    menu_options = {
        1: 'Balance',
        2: 'Log out',
        0: 'Exit'
    }

    # todo think about duplicated code
    def print_menu(self):
        for key in self.menu_options.keys():
            print(f'{key}. {self.menu_options[key]}')

    def option1(self):
        print(f'Balance: {self.balance}')

    @staticmethod
    def option2():
        print('You have successfully logged out!')

    @staticmethod
    def option3():
        print('Bye')
        exit()
