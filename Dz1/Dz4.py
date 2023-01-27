# Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

print('Введите количество долек по горизонтали:')
horizontally = int(input())
print('Введите количество долек по вертикали:')
vertically = int(input())
print('сколько хотите отрезать долек?')
break_off = int(input())
if break_off>(horizontally*vertically)-vertically:
    print('столько отрезать нельзя')
elif break_off < vertically:
    print('столько отрезать нельзя')
elif break_off % vertically != 0:
    print('столько отрезать нельзя')
else:
    print('столько отрезать можно')