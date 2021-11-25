
# Task_2 (script_1)

# Написати функцію, яка отримує на вхід список, на вихід повертає True
# – якщо в списку є більше ніж 5 трьохзначних чисел, інакше False


list_1 = [14, 15, 23, 124, 14414, 12234, 123, 11, 1]
list_2 = [123, 1, 1234, 1234, 22234, 143553, 112, 1]
list_3 = [123, 234, 1, 2, 3, 345, 2114, 242445, 2, 523]

def chisla_1(list):
    num3 = 0
    for i in list:
        if len(str(i)) >= 3:
            num3 += 1
    if num3 > 5:
        return True
    else:
        return False


print(chisla_1(list_1))
print(chisla_1(list_2))
print(chisla_1(list_3))

