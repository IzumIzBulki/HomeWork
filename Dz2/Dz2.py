# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму 
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3

from random import randint as RI

first_number = RI(1, 1000)
print(f"Первое задуманное число: {first_number}")
second_number = RI(1, 1000)
print(f"Второе задуманное число: {second_number}")
first_clue = 0
second_clue = 0
first_clue = first_number + second_number
print(f"Первая подсказка(сумма): {first_clue}")
second_clue = first_number * second_number
print(f"Вторая подсказка(произведение): {second_clue}")

first_guessed_number = first_clue // 2
second_guessed_number = first_clue - first_guessed_number

while second_clue != first_guessed_number * second_guessed_number:
    first_guessed_number -= 1
    second_guessed_number += 1

if first_number > second_number:
    print(f"Первое задуманное число: {second_guessed_number}, \
    Второе задуманное число: {first_guessed_number}")
else:
    print(f"Первое задуманное число: {first_guessed_number}, \
    Второе задуманное число: {second_guessed_number}")
