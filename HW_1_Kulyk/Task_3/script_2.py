
# Task_3 (script_2)

# Є списки list_1 = [1, 2, 3, 4, 5, 6] list_2 = [1, 4, 9]. Написати скрипт який
# виведе на екран: елементи які є в list_2, але відсутні в list_1; тільки ті
# елементи які є в двох списках; всі елементи які є в двох списках;
# елементи яких немає одночасно в двох списках.

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [1, 4, 9]
result = set(list_2) - set(list_1) # елементи які є в list_2, але відсутні в list_1;
result_2 = set(list_1) & set(list_2)  # тільки ті елементи які є в двох списках;
result_3 = set(list_2) | set(list_1) # всі елементи які є в двох списках;
result_4 = set(list_1) ^ set(list_2) # елементи яких немає одночасно в двох списках.
print(result)
print(result_2)
print(result_3)
print(result_4)
