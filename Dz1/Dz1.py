print('Введите число:'); 
number = int(input())
summ_numbers = 0
while number >999 or number <= 99:
    print('Введите трехзначное число')
    number =  int(input())
while number>0:
    summ_numbers = summ_numbers + number%10
    number=int(number/10)
print(summ_numbers); 
