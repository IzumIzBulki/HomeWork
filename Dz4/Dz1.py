# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

ferst_length_list = int(input("Введите длину первого списка: "))
second_length_list = int(input("Введите длину второго списка: "))
ferst_numbers = list()
second_numbers = list()
while ferst_length_list != 0:
    ferst_numbers.append(input("Введите значение для первого списка: "))
    ferst_length_list -=1
print("Заполнение первого списка закончилось")
while second_length_list != 0:
    second_numbers.append(input("Введите значение для второго списка: "))
    second_length_list -=1
print("Заполнение второго списка закончилось")  
dictionary = {} 
final_list = []
for letter in ferst_numbers:
    dictionary[letter] = dictionary.get(letter, 0) + 1
for letter in second_numbers:   
    dictionary[letter] = dictionary.get(letter, 0) + 1
for letter in dictionary:
    if dictionary[letter] > 1:
        final_list.append(letter)
final_list.sort()
print("Совпадений нет" if len(final_list) == 0 else f'Список [{" ".join(final_list)}]')  







# ferst_numbers = input("Введите первый набор чисел через пробел: ")
# second_numbers = input("Введите второй набор чисел через пробел: ")
# ferst_list = set(ferst_numbers.split())   
# second_list = set(second_numbers.split())
# dictionary = {} 
# final_list = []
# for letter in ferst_list:
#     dictionary[letter] = dictionary.get(letter, 0) + 1
# for letter in second_list:   
#     dictionary[letter] = dictionary.get(letter, 0) + 1
# for letter in dictionary:
#     if dictionary[letter] > 1:
#         final_list.append(letter)
# print("Совпадений нет" if len(final_list) == 0 else f'Список [{" ".join(final_list)}]')  
