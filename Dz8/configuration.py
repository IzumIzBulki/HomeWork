import os
global book
book = 'book.txt'

def menu():
    print("\n1: Показать контакты")
    print("2: Добавить контакт")
    print("3: Изменить контакт")
    print("4: Найти контакт")
    print("5: Удалить контакт")
    print("0: Выход")
   
def treatment(number):
    if number == 1:
        print("\nВы перешли в меню Показать контакты")
        open_book()
    elif number == 2:
        print("\nВы перешли в меню Добавить контакт")
        add_in_book()
    elif number == 3:
        print("\nВы перешли в Изменить контакт")
        change_contact()
    elif number == 4:
        print("\nВы перешли в Найти контакт")
        search()
    elif number == 5:
        print("\nВы перешли в Удалить контакт")
        deleted()

# Изменить контакт
def change_contact():
    item_menu = input("Выберите фамилию или номер телефона которую требуется изменить: ")
    new_item_menu = input("Выберите новую фамилию или номер телефона: ")
    with open (book, 'r', encoding='utf-8') as b:
        old_data = b.read()
    new_data = old_data.replace(item_menu, new_item_menu, 1)
    with open (book, 'w', encoding='utf-8') as b:
        b.write(new_data)
    print(f"контакт: {item_menu}\nбыл изменен на: {new_item_menu}")
   
# Удалить контакт
def deleted():
    item_menu = input("Выберите фамилию или номер телефона которую желаете удалить: ")
    with open(book, encoding='utf-8') as in_file, open("output.txt", "w", encoding='utf-8') as out_file:
        for line in in_file:
            line = line.split()
            if line[0] == item_menu:
                print(f"Контакт [ {' '.join(line)} ] удален")
            elif line[-1] == item_menu:
                print(f"Контакт [ {' '.join(line)} ] удален")
            else:
                out_file.write(f"{' '.join(line)}\n")
    os.remove('book.txt')
    os.rename("output.txt", 'book.txt')

# Найти контакт
def search():
    item_menu = input("Выберите фамилию или номер телефона: ")
    data = open(book, 'r', encoding='utf-8')
    for line in data:
        line = line.split()
        if line[0] == item_menu:
            print(' '.join(line))
        if line[-1] == item_menu:
            print(' '.join(line))
    data.close()

# Добавить контакт
def add_in_book():
    surname = input("Введи фамилию: ")
    numbers = input("Введи номер: ")
    data = open(book, 'a', encoding='utf-8')
    data.write(f'\n{surname}\t|\t')
    data.write(f"{numbers}")
    print("Контакт успешно добавлен")

# Показать контакты
def open_book():
    data = open(book, 'r', encoding='utf-8')
    for line in data:
        print(' '.join(line.split()))
    data.close()

