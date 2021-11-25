
# Task_2 (script_3)

# Написати функцію що приймає на вхід список чисел. Функція повинна
# повернути кількість елементів в цьому списку, які більші ніж два їх
# сусіди. Крайні елементи списку ніколи не враховуються, оскільки у них
# недостатньо сусідів

list_1 = [10, 20, 5, 40, 90, 1, 312, 999, 131, 23, 11, 717]
list_2 = [2, 1]
list_3 = [2, 5, 3]

def bolshe(list):
    schet = 0
    if len(list) <= 2:
        return ("You should enter 3+ int!")
    else:
        for i in list[1:-1]:
            if list[list.index(i)] > list[list.index(i)-1] and list[list.index(i)] > list[list.index(i)+1]:
                schet += 1
            else:
                pass
    return schet


print(bolshe(list_1))

