# Напишите программу, которая на вход принимает два числа A и B, и 
# возводит число А в целую степень B с помощью рекурсии. >

def sum(number, rank, product):
    if rank == 0:
        return product 
    return sum(number, rank-1, product*number)

number = int(input("Введите число: "))
rank = int(input("Введите степень: "))
print(f'число {number} в степени {rank} = {sum(number, rank, 1)}')