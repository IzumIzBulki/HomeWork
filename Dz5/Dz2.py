# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum_numbers(sum, second_number):
    if second_number == 0:
        return sum
    return sum_numbers(sum+1, second_number-1)

sum = int(input("Введите число А: "))
second_number = int(input("Введите число В: "))

print(f'сумма числа {sum} и {second_number} = {sum_numbers(sum, second_number)}')