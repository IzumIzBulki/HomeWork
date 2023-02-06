# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint as RI

length_list = int(input("Введите длину списка: "))
number = int(input("Введите искомое число: "))
list = list()
count = 0
first_max = 100
first_min = 0
second_max = 0
second_min = 0
for i in range(0, length_list, 1):
    list.append(RI(1, 10))
    if list[i] == number:
        count += 1
    elif  list[i] > number  and list[i] < first_max :
        first_max = list[i]
    elif list[i] > first_min and list[i] < number :
        first_min = list[i]

if count !=0:
    print(f'количество повторяющихся чисел = {count} \n{list}')
elif first_min == 0:
    print(f'ближайшее число = {first_max} \n{list}') 
else:
    second_min = number - first_min
    second_max = first_max - number
    if second_max > second_min:
        print(f'ближайшее число = {first_min} \n{list}')
    else:
        print(f'ближайшее число = {first_max} \n{list}') 



