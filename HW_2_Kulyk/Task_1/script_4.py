
# Task_1 (script_4)

# Напишіть скрипт який отримає
# від користувача рядок з текстом, порахує скільки раз, кожна літера з
# алфавіту повторюється в тексті. Якщо літера жодного разу не
# повторилась, все одно вивести кількість повторень (0)
# Вивід повинен мати подібний вивід
# a: 12
# b: 23
# c: 4
# d: 0
# …
# Тобто на екран виводити форматований текст, а не просто прінт
# колекції)

import collections

def alfavit_2(text):
    list_1 = []
    dict_1 = {}
    for i in text:
        list_1.append(i.lower())
    for i in range(97, 123):
        dict_1.update([(chr(i), i)])
        if chr(i) in text:
            dict_1.update([(chr(i),collections.Counter(list_1)[chr(i)] )])
        else:
            dict_1.update([(chr(i), 0)])
        print(chr(i), ":",collections.Counter(list_1)[chr(i)] )

alfavit_2("Hello World!")










