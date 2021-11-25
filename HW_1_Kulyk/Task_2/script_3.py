
# Task_2 (script_3)

# Написати скрипт який має константу рядок на 10 символів (наприклад
# "qwertyuiop"), на екран виводимo перший символ строки, останній
# символ рядка, перші 3 символи рядка, 2-6 символи рядка. Вивід
# повинен мати вигляд:
# q
# p
# qwe
# werty

text = "qwertyuiop"
text = list(text)
print(text[0])
print(text[9])
a = text[0:3]
print("".join(a))
b = text[1:6]
print("".join(b))

