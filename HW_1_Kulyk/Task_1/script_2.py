
# Task_1 (script_2)
# Написати скрипт, який запитує в користувача число а, потім число b і
# виводить на екран повідомлення про те, яке число більше. Можна
# використовувати тільки оператори порівняння!

print("\nПривіт! Ця програма допоможе тобі розібратися яке число більше.")

a = int(input("\nВведіть перше число для порівняння: "))
b = int(input("\nТепер введіть друге число: "))

if a > b:
    print("Число",a,"більше чим число",b)
elif b > a:
    print("Число",b,"більше чим число",a)
else:
    print("Схоже число",a,"і",b,"- рівні!")

