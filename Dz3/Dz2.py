# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков

#     Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#     Будем считать, что на вход подается только одно слово, которое содержит либо
#     только английские, либо только русские буквы.

import copy

En_library = [{"1": "AIEOULNSTR"},{"2": "DG"},{"3": "BCMP"},{"4": "FHVWY"},
            {"5": "K"},{"8": "JX"},{"10": "QZ"}]
Ru_library = [{"1": "АВЕИНОРСТ"},{"2": "ДКЛМПУ"},{"3": "БГЁЬЯ"},{"4": "ЙЫ"},
            {"5": "ЖЗХЦЧ"},{"8": "ШЭЮ"},{"10": "ФЩЪ"}]
word = input("Введите слово: ").upper()
summ = 0
count = 0

if 65 <= ord(word[0]) <= 90:
    for list in word: # перебираю каждую букву введенного слова
        for item in En_library: # перебираю словари в библиотеке
            if summ != count:  # прерывает поиск букв, если найдено одно совпадение, уменьшает количество итераций и работы(не проверяет ненужные буквы)
                    count = copy.copy(summ)
                    break
            for key in item: # перебираю словари по ключам
                for letter in item[key]:  # перебираю буквы в словарях
                    if list == letter:
                        summ += int(key)
                        break 
else:
    for list in word: # перебираю каждую букву введенного слова
        for item in Ru_library:   # перебираю словари в библиотеке 
            if summ != count:  # прерывает поиск букв, если найдено одно совпадение, уменьшает количество итераций и работы(не проверяет ненужные буквы)
                    count = copy.copy(summ)
                    break                    
            for key in item:        # перебираю словари по ключам               
                for letter in item[key]: # перебираю буквы в словарях
                    if list == letter:
                        summ += int(key)
                        break
print(f"сумма букв = {summ}")