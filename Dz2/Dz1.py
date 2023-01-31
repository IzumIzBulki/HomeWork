# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а 
# некоторые – гербом. Определите минимальное число монеток, которые 
# нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
# 2
from random import randint as RI
number_coins = int(input())
number_eagle = 0
number_tails = 0
side = 0
n = 0
while n < number_coins:
    side = RI(0, 1)
    print(side, end=' ')
    if side == 0:
        number_tails += 1
    else:
        number_eagle += 1
    n += 1
if number_tails > number_eagle:
    print(f"минимально надо перевернуть {number_eagle} монет (орел)")
else:   
    print(f"минимально надо перевернуть {number_tails} монет (решка)")

