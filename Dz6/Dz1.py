# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

ferst_element = int(input("Введите первый элемент: "))
step = int(input("Введите шаг: "))
count = int(input("Введите количество элементов: "))
list = []
def summ(f, s, c, l):
    if c == 0:
        return
    return l.append(f), summ(f+s, s, c-1, l)
summ(ferst_element, step, count, list)
print("Наша прогрессия:", list)

