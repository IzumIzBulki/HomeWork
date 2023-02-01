# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input("Введите число: "))
degree = 0
number_degree = 1
while degree < number:
    number_degree = 2**degree
    degree += 1
    if number_degree > number:
        break
    print(number_degree, end=' ')
    