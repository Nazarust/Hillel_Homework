
# Task_4 (script_1)

# Є словник dict_1 = {1: “apple”, 2: “Samsung”, 3: “HP”, 4:”HTC”,
# 5:”Xiaomi”}.
# Користувач вводить число, якщо такий ключ є в словнику, то вивести
# на екран значення, інакше, вивести повідомлення що такого ключа не
# існує


dict_1 = {1: "apple", 2: "Samsung", 3: "HP", 4: "HTC", 5: "Xiaomi"}
number = 0

print("Натисніть '0',щоб вийти!")

while number == 0:
    choose = int(input("Зробіть вибір ключа: "))
    if choose == 0:
        print("До побачення!")
        break
    elif choose in dict_1.keys():
        print(dict_1[choose])
    else:
        print("Такого ключа не існує!")

