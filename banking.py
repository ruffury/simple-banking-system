from start_menu import StartMenu

menu = StartMenu()
while True:
    menu.print_menu()
    option = int(input())
    if option == 1:
        menu.option1()
    elif option == 2:
        menu.option2()
    else:
        exit()
