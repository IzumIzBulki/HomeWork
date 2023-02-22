# ; Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# ; Поскольку разобраться в его кричалках не настолько просто, 
# ; насколько легко он их придумывает, Вам стоит написать программу. 
# ; Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# ; в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# ; если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# ; Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# ; если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
# ; Ввод: пара-ра-рам рам-пам-папам па-ра-па-да

# ; Вывод: Парам пам-пам


poesy = input("Введите фразы через пробел, слова во фразе разделите - : ").split()
vowels = []
for phrase in poesy:
    count = 0
    for letter in phrase:
        if letter in ["а","я","у","ю","о","е","ё","э","ы","и"]:
            count +=1
    if count > 0:
        vowels.append(count)
print("Парам пам-пам" if len(set(vowels)) == 1 else "Пам парам")