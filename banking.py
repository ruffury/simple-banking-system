from start_menu import StartMenu

if __name__ == '__main__':

    menu = StartMenu()
    while True:
        menu.print_menu()
        option = int(input())
        if option == 1:
            menu.option1()
        else:
            exit()