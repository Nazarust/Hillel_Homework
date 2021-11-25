
# Task_3 (script_3)

# Написати функцію яка приймає на вхід аргумент ціле число n і створює
# список цілих чисел від 0 до n. Написати до цієї функції декоратор який всі
# елементи отриманого списку переведе в тип даних - рядок


def decor_for_number(func):
    def wrapper(num):
        new_list = []
        result = func(num)
        for i in result:
            i = str(i)
            new_list.append(i)
        print(new_list)
        return new_list
    return wrapper


@decor_for_number
def number(n):
    list = []
    num = 0
    while num <= n:
        list.append(num)
        num += 1
    return list

number(10)
number(20)

