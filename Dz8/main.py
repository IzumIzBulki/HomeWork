import configuration as conf



def start():
    conf.menu()
    item_menu = int(input("\nВыберите пункт меню: "))
    while item_menu != 9:
        conf.treatment(item_menu)
        conf.menu()
        item_menu = int(input("\nВыберите пункт меню: "))
    print("\nВы вышли из программы")