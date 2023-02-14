# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint as RI

length_list = int(input("Введите длину списка: "))
range_from = int(input("Введите диапазон поиска от: "))
range_before = int(input("Введите диапазон поиска до: "))
list = []
list_index = []
list_numbers = []
i = 0
while length_list != 0:
    list.append(RI(1, 10))
    if list[i] >= range_from and list[i] <= range_before:
        list_index.append(i)
        list_numbers.append(list[i])
    i += 1
    length_list -= 1
print(f'Созданный список: {list}')
print(f'Индексы значений, которые находятся в диапазоне от {range_from} до {range_before}: {list_index} \n\
значения: {list_numbers}')

    
