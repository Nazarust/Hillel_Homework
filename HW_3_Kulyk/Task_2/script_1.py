
# Task_2 (script_1)

# в file_2 лежить список чисел, в вигляді байткоду. Отримайте даний список
# і знайдіть кількість чисел паліндромів. Паліндром це число яке зліва на право
# і справа на ліво читається однаково.

import pickle


def open_pickle(file):
    with open(f'{file}', 'rb') as f:
        data_new = pickle.load(f)
    return data_new


def find_int(file):
    a = open_pickle(file)
    result = 0
    for i in a:
        i = list(str(i))
        if i == i[::-1]:
            my_string = ''.join(i)
            result += 1
            print(my_string, "- yes")
        else:
            my_string = ''.join(i)
            print(my_string, "- no")
    return f"Кількість чисел паліндромів : {result} "


print(find_int("file_2"))



