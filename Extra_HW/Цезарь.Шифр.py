alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavit_UA = ' АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
check = None

while check != 0:
    print("""
           Меню   
    0 - Вийти з програми
    1 - Зашифрувати повідомлення
    2 - Розшифрувати повідомлення""")
    check = int(input("Ваш вибір: "))
    if check == 0:
        print("До побачення!")
        break
    elif check == 1:
        smeshenie = int(input("Крок шифрування: "))
        message = input("Повідомлення для шифровки: ").upper()
        itog = ''
        lang = input("Виберіть мову RU/EU/UA: ")

        if lang == "RU":
            for i in message:
                if i in alfavit_RU:   
                    itog += alfavit_RU[(alfavit_RU.index(i) + smeshenie) % len(alfavit_RU)]
                else:
                    itog += ' '
        elif lang == "EU":
            for i in message:
                if i in alfavit_EU:
                    itog += alfavit_EU[(alfavit_EU.index(i) + smeshenie) % len(alfavit_EU)]
                else:
                    itog += ' '
        elif lang == "UA":
            for i in message:
                if i in alfavit_UA:
                    itog += alfavit_UA[(alfavit_UA.index(i) + smeshenie) % len(alfavit_UA)]
                else:
                    itog += ' '
        print(itog)
    elif check == 2:
        smeshenie = int(input("Крок шифрування: "))
        message = input("Повідомлення для розшифровки: ").upper()
        itog = ''
        lang = input("Виберіть мову RU/EU/UA: ")
        if lang == "RU":
            for i in message:
                if i in alfavit_RU:
                    itog += alfavit_RU[(alfavit_RU.index(i) - smeshenie) % len(alfavit_RU)]
                else:
                    itog += ' '
        elif lang == "EU":
            for i in message:
                if i in alfavit_EU:
                    itog += alfavit_EU[(alfavit_EU.index(i) - smeshenie) % len(alfavit_EU)]
                else:
                    itog += ' '
        elif lang == "UA":
            for i in message:
                if i in alfavit_UA:
                    itog += alfavit_UA[(alfavit_UA.index(i) - smeshenie) % len(alfavit_UA)]
                else:
                    itog += ' '
        print(itog)


