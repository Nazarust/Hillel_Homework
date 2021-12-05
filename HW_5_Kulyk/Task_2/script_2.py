
# Напишіть нескінченний генератор ідентифікаторів, ID створюється по
# шаблону “{prefix}-{number}”. Де prefix – рядок що отримується від
# користувача, а number – інкремент.
# Приклад використання – в генератор передається префікс ID, генератор
# при кожному звернені повертає
# ID-1
# ID-2
# ID-3
# якщо префікс INTERNAL-ID
# INTERNAL-ID-1
# INTERNAL-ID-2
# INTERNAL-ID-3
# і тд.
# Якщо префікс не передається то повертати потрібно тільки інкремент
# 1
# 2
# 3
# Генератор завжди повертає тип даних string!

def id_generator(prefix=""):
    i = 1
    if prefix != "":
        prefix = prefix + "-"
    while True:
        yield f"{prefix}{i}"
        i += 1