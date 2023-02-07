# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

string1 = '1 2 33 32 2 1 5 66'
string2 = '4 5 66 6 43 3 1 2'
my_list1 = string1.split()    #перевести в список и разделить пробелами, split()разделяет по умолчанию пробелами или тем, что указать в ()
my_list2 = string2.split()
new_list1 = set(my_list1)
new_list2 = set(my_list2)
my_dict1 = {} #пустой словарь
new_list4 = []
for letter in new_list1:
    my_dict1[letter] = my_dict1.get(letter, 0) + 1
for letter in new_list2:   
    my_dict1[letter] = my_dict1.get(letter, 0) + 1
for letter in my_dict1:
    if my_dict1[letter] > 1:
        new_list4.append(letter)
print(new_list4)  









# my_dict1 = {} #пустой словарь
# my_dict2 = {} #пустой словарь
# new_list1 = [] #пустая строка
# new_list2 = [] #пустая строка

# for letter in my_list1:
#     my_dict1[letter] = my_dict1.get(letter, 0) + 1
# for letter in my_list2:   
#     my_dict2[letter] = my_dict2.get(letter, 0) + 1
# for letter in my_dict1:
#     new_list1.append(letter)
# for letter in my_dict2:
#     new_list2.append(letter)

# print(my_list3)  
# print(my_list1)
# print(my_dict1) 
# print(new_list1) 

