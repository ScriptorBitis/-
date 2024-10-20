# -*- coding: utf-8 -*-
import re

print('\nВариант лабораторной работы для выполнения третьего задания:', 467969 % 8 )
print('''Задание:
С помощью регулярного выражения найти в тексте слова, в которых встречается строго одна гласная буква (встречаться она может несколько раз). 
Пример таких слов: окно, трава, молоко, etc.
После чего данные слова требуется отсортировать сначала по увеличению длины слова, а затем лексикографически.
''')
cnt=0
def third_task(string):
    global cnt
    cnt+=1
    print(f'Тест номер {cnt} \n {string} \n Ответ:')


    string=string.lower()
    letters = 'аеиоуыэюя'
    some_funny_array = []
    for i in letters:
        pattern = fr"\b[{i}бвгджзклмнпрстфхцчшщъь]+\b"
        some_funny_array.append(re.findall(pattern, string))


    while [] in some_funny_array:
        some_funny_array.remove([])
    print(some_funny_array)

    #получили значение-надо выводить
    new_array = []
    for i in some_funny_array:
        for j in i:
            new_array.append(j)
    print(new_array)

    new_array.sort(key=lambda x:(len(x),x))
    #отсортировать сначала по увеличению длины слова, а затем лексикографически

    print(new_array)
    #print(some_funny_array)
    #print(new_array)

    for i in new_array:
        print(i)

test_three = ["Классное слово – обороноспособность, которое должно идти после слов: трава и молоко.",
              ]

for test3 in test_three:
    third_task(test3)
