from start_menu import StartMenu

menu = StartMenu()
while True:
    menu.print_menu()
    option = input()
    if option == '1':
        menu.create_account()
    elif option == '2':
        menu.log_into_account()
    else:
        exit()
