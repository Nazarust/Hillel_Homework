
# Task_2 (script_1)

# Написати скрипт для підрахунку кількості слів у введеному з
# клавіатури рядку. Словом вважати послідовність символів, що
# відокремлену символами пропуску.

a = input("Ведіть речення: ")
a = a.split()
print("В вашому реченні",len(a),"слів!")