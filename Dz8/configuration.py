


def menu():
    print("1: Открыть книгу")
    print("2: Сохранить файл")
    print("3: Показать контакты")
    print("4: Добавить контакт")
    print("5: Изменить контакт")
    print("6: Найти контакт")
    print("7: Удалить контакт")
    print("8: Создать новый файл")
    print("9: Выход")
   
def treatment(number):
    if number == 1:
        print("\nВы перешли в Открыть книгу")
        open_book()
    elif number == 2:
        print("\nВы перешли в Сохранить файл")
    elif number == 3:
        print("\n3: Показать контакты")
    elif number == 4:
        print("\nВы перешли в меню Добавить контакт")
        add_in_book()
    elif number == 5:
        print("\nВы перешли в Изменить контакт")
    elif number == 6:
        print("\nВы перешли в Найти контакт")
        search()
    elif number == 7:
        print("\nВы перешли в Удалить контакт")
        deleted()
    else: 
        number == 8
        print("\nВы перешли в Создать новый файл")
  
# удаление контакта
def deleted():
    item_menu = input("Выберите фамилию или номер телефона которую желаете удалить: ")
    data = open('book.txt', 'r')
    for line in data:
        line = line.split()
        if line[0] == item_menu:
            print(f"Контакт [ {' '.join(line)} ] удален")
            line.clear()
        elif line[-1] == item_menu:
            print(f"Контакт {' '.join(line)} удален")
            line.clear()
    print()
    data.close()

# поиск контакта
def search():
    item_menu = input("Выберите фамилию или номер телефона: ")
    path = 'book.txt'
    data = open(path, 'r')
    for line in data:
        line = line.split()
        if line[0] == item_menu:
            print(' '.join(line))
        if line[2] == item_menu:
            print(' '.join(line))
    data.close()

# запись в файл
def add_in_book():
    colors1 = input("Введи фамилию: ")
    colors2 = input("Введи номер: ")
    data = open('book.txt', 'a')
    data.write(f'{colors1} |')
    data.write(f" {colors2} \n")
    print("Контакт успешно добавлен \n")

# чтение из файла
def open_book():
    path = 'book.txt'
    data = open(path, 'r')
    for line in data:
        print(line)
    data.close()

