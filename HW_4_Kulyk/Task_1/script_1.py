
# Реалізуйте три ролі користувачів групи соцмереж (Admin, Moderator,
# Member). Обєкти віх ролей повинні мати такі однакові атрибути –
# name, surname, age, join_date, user_id. Модератор і адмін мають
# додатково атрибут badge (значок, або щось типу статусу, по суті просто
# текст). Адмін має додатковий атрибут level.
# Також у всіх повинна бути можливість отримати full_name – (name +
# surname).
# name, surname, age, join_date – заповнюються при створені, приходять
# як аргументи в конструктор. badge – опціонально. Level – відразу
# ставиться в значення 1, але можна змінювати після створення
# Всі користувачі можуть змінювати своє name, surname, age, badge(адмін
# і модератор) і level(для адміна). join_date, user_id – змінювати
# забороняється будь-кому.










# ДЛЯ ЗАПУСКУ КОНТЕКСТНОГО МЕНЮ ЗАПУСТІТЬ ФУНКЦІЮ main_global() В КІНЦІ ЦЬОГО ФАЙЛУ





import datetime
import random

def new_id():
    new_id = ""
    while len(new_id) < 9:
        i = random.randint(0, 9)
        new_id += str(i)
    return new_id


class Member(object):
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.full_name = str(self.name + " " + self.surname)
        self.age = age
        self.__join_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        self.__user_id = new_id()

    @property
    def user_id(self):
        return self.__user_id

    @property
    def join_date(self):
        return self.__join_date

    def new_name(self):
        new_name = input("Enter your new name: ")
        if new_name == "":
            print("You should to enter name!")
        else:
            self.name = new_name
            self.full_name = str(self.name + " " + self.surname)

    def new_surname(self):
        new_surname = input("Enter your new surname: ")
        if new_surname == "":
            print("You should to enter surname!")
        else:
            self.surname = new_surname
            self.full_name = str(self.name + " " + self.surname)

    def new_age(self):
        new_age = int(input("Enter new age: "))
        if new_age < 18:
            print("You must have 18 years old!")
        else:
            self.age = new_age

class Moderator(Member):
    def __init__(self, name, surname, age, badge="online"):
        super(Moderator, self).__init__(name, surname, age)
        self.badge = badge

    def new_badge(self):
        new_badge = input("Enter your new badge: ")
        self.badge = new_badge


class Admin(Moderator):
    def __init__(self, name, surname, age, badge="online", level=1):
        super(Admin, self).__init__(name, surname, age, badge)
        self.level = level
        self.badge = badge

    def new_level(self):
        new_level = int(input("Enter your new level: "))
        self.level = new_level


def main_global():
    chose = ""
    while chose != "0":
        print("""
        Welcome to our system!
        0 - Exit
        1 - Create Member
        2 - Create Moderator
        3 - Create Admin
        """)
        chose = input("Enter your answer: ")
        if chose == "0":
            break
        elif chose == "1":
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            age = int(input("Enter age: "))
            member = Member(name, surname, age)
            main_member(member)
        elif chose == "2":
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            age = int(input("Enter age: "))
            moderator = Moderator(name, surname, age)
            main_moderator(moderator)
        elif chose == "3":
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            age = int(input("Enter age: "))
            admin = Admin(name, surname, age)
            main_admin(admin)


def main_member(member):
    chose = ""
    while chose != "0":
        print("""
        Welcome to Member settings!
        0 - Exit
        1 - See info
        2 - Change name
        3 - Change surname
        4 - Change age
        """)
        chose = input("Your answer: ")
        if chose == "0":
            break
        elif chose == "1":
            print(f"""
            Name: {member.name}
            Surname: {member.surname}
            FullName: {member.full_name}
            Age: {member.age}
            Date: {member.join_date}
            ID: {member.user_id}""")
        elif chose == "2":
            member.new_name()
        elif chose == "3":
            member.new_surname()
        elif chose == "4":
            member.new_age()


def main_moderator(moderator):
    chose = ""
    while chose != "0":
        print("""
           Welcome to Member settings!
           0 - Exit
           1 - See info
           2 - Change name
           3 - Change surname
           4 - Change age
           5 - Change badge
           """)
        chose = input("Your answer: ")
        if chose == "0":
            break
        elif chose == "1":
            print(f"""
            Name: {moderator.name}
            Surname: {moderator.surname}
            FullName: {moderator.full_name}
            Age: {moderator.age}
            Date: {moderator.join_date}
            ID: {moderator.user_id}
            Badge: {moderator.badge}""")
        elif chose == "2":
            moderator.new_name()
        elif chose == "3":
            moderator.new_surname()
        elif chose == "4":
            moderator.new_age()
        elif chose == "5":
            moderator.new_badge()


def main_admin(admin):
    chose = ""
    while chose != "0":
        print("""
               Welcome to Member settings!
               0 - Exit
               1 - See info
               2 - Change name
               3 - Change surname
               4 - Change age
               5 - Change badge
               6 - Change level
               """)
        chose = input("Your answer: ")
        if chose == "0":
            break
        elif chose == "1":
            print(f"""
                Name: {admin.name}
                Surname: {admin.surname}
                FullName: {admin.full_name}
                Age: {admin.age}
                Date: {admin.join_date}
                ID: {admin.user_id}
                Badge: {admin.badge}
                Level: {admin.level}""")
        elif chose == "2":
            admin.new_name()
        elif chose == "3":
            admin.new_surname()
        elif chose == "4":
            admin.new_age()
        elif chose == "5":
            admin.new_badge()
        elif chose == "6":
            admin.new_level()



# main_global()
