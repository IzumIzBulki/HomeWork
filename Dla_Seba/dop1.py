# В этой задаче вам предлагается реализовать сортировку выбором.

# Задан массив целых чисел a0, a1, …, an−1. Отсортируем его следующим образом:

# выберем наибольший элемент массива и поменяем его местами с последним элементом 
# (если последний и есть найденный максимум, то обмен можно не совершать),
# исключим из рассмотрения последний элемент и если длина оставшегося участка 
# больше нуля перейдем опять к предыдущему пункту.
# Таким образом, этот алгоритм состоит их n фаз, на каждой из которых 
# выбирается максимум. Ваша задача реализовать эту сортировку описанным способом и 
# вывести n чисел — индексы максимума на каждой из n фаз. Если максимум встречается 
# более одного раза, то надо всегда выбирать первый из них.

# Входные данные
# В первой строке входного файла INPUT.TXT задано одно целое число n (1 ≤ n ≤ 1000) — количество 
# элементов в массиве. Во второй строке задано n целых чисел 
# через пробел: a0, a1, …, an−1 (|ai| ≤ 109) — элементы массива.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите n чисел через пробел, где число i — это индекс первого максимального 
# элемента на i-й фазе алгоритма.


array_length = int(input())
array = []
n = 0

while n != array_length:
    list.insert(n, n)
    n+=1
print(array)

