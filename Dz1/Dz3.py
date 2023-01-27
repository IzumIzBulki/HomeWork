# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным
# номером, где сумма первых трех цифр равна сумме последних трех. Т.е.
# билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

print('Введите номер билетика:')
number = int(input())
summ_numbers_left = 0
summ_numbers_right = 0
while number > 999999 or number <= 99999:
    print('Введите шестизначное число')
    number = int(input())
while number > 999:
    summ_numbers_right = summ_numbers_right + number % 10
    number = int(number/10)
while number > 0:
    summ_numbers_left = summ_numbers_left + number % 10
    number = int(number/10)
if summ_numbers_left == summ_numbers_right:
    print("Билетик удачный")
else: 
    print("Билетик неудачный")

