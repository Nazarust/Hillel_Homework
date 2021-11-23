
# Task_3 (script_2)

# Написати функцію яка приймає список елементів і знаходить суму, до
# функції написати декоратор який перед тим як запустити функцію видаляє з
# списку всі не чисельні типи даних, але якщо є рядок який можна перевести в
# число, (наприклад “1”, “24.3”) то рядок приводиться до чисельного типу
# даних

list_1 = [2, 2, 2, "dwdwd", "2", 2]

def decor_suma(func):

    def wrapper(list):
        list_decor = []
        for i in list:
            try:
                if float(i):
                    list_decor.append(float(i))
            except:
                continue

        result = func(list_decor)
        print(f"Сума всіх чисел в списку: {result} ")

        return result

    return wrapper



@decor_suma
def suma(list):
    result = 0
    for i in list:
        result += i
    return result


suma(list_1)

