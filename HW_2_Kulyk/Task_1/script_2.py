
# Task_1 (script_2)

# Написати скрипт, який в циклі на кожній ітерації отримує від
# користувача з клавіатури числа, до тих пір, поки користувач не введе 0.
# Після завершення роботи циклу, порахувати середнє арифметичне всіх
# введених чисел. Число 0 не повинно враховуватись в підрахунку
# середнього арифметичного. Зверніть увагу що користувач може давати
# рядки в яких містяться не тільки цифри. Такі рядки не потрібно
# використовувати в обчисленнях

num_1 = []
choice = None
suma = []


def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


while choice != "0":
    choice = input("Введіть цифру(0 для закінчення): ")
    num_1.append(choice)
    if not is_digit(choice):
        num_1.remove(choice)
    elif choice == "0":
        num_1.remove("0")

for item in num_1:
    suma.append(float(item))
print(sum(suma) / len(suma))




