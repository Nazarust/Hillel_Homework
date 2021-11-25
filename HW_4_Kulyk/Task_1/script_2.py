
# В файлі hw_data.py лежать «заглушки» функцій для роботи в групі.
# Реалізуйте розмежування доступу. Якщо доступ заборонений –
# print(«forbidden»).
# Member – може ставити лайк, і шейрити статтю
# Moderator – те ж що і Member, + створювати і оновлювати статтю
# Admin – те ж що і Moderator+ видаляти статтю і видаляти групу. Проте
# видаляти групу може адміністратор рівня не менше ніж 3
# Для реалізації розмежування ви можете дописувати функції, проте
# найкращим варіантом буде реалізувати перевірку на доступ через
# декоратори.


from script_1 import Member, Moderator, Admin


def share_and_like_wrapper(func):

    def wrapper(user, *args):
        try:
            if user.name:
                print(user.name + ":")
                func(user, args)
        except AttributeError:
            print(user.name + ":")
            print("forbidden\n")

    return wrapper


def update_and_create_wrapper(func):

    def wrapper(user, *args):
        try:
            if user.badge:
                print(user.name + ":")
                func(user, *args)
        except AttributeError:
            print(user.name + ":")
            print("forbidden\n")

    return wrapper


def delete_article_wrapper(func):

    def wrapper(user, *args):
        try:
            if user.level:
                print(user.name + ":")
                func(user, *args)
        except AttributeError:
            print(user.name + ":")
            print("forbidden\n")

    return wrapper

def delete_group_wrapper(func):

    def wrapper(user, *args):
        try:
            if user.level:
                if user.level >= 3:
                    print(user.name + ":")
                    func(user, *args)
                else:
                    print(user.name + f",your level is {user.level}:")
                    print("forbidden\n")
        except AttributeError:
            print(user.name + ":")
            print("forbidden\n")

    return wrapper


@delete_group_wrapper
def delete_group(user, group_id):
    print("Group has been deleted\n")

@delete_article_wrapper
def delete_article(user, article_id):
    print("Article has been deleted\n")

@update_and_create_wrapper
def create_article(user, post_data):
    print("Article has been created\n")

@update_and_create_wrapper
def update_article(user, update_data):
    print("Article has been updated\n")

@share_and_like_wrapper
def share_article(user, article_id):
    print("Article has been shared\n")

@share_and_like_wrapper
def set_like_to_article(user, post_data):
    print("Like has been set\n")


Nazar_Admin = Admin("Nazar", "Kulyk", 21, "online", 2)
Egor_Moderator = Moderator("Egor", "Bushak", 34, "offline")
Lena_Member = Member("Lena", "Garsha", 20)
Zakhar_Admin = Admin("Zakhar", "Rebinto", 35, "online", 5)

set_like_to_article(Lena_Member, 22445)
share_article(Nazar_Admin, 234255)
share_article(Egor_Moderator, 23245)
update_article(Lena_Member, 23245)
update_article(Egor_Moderator, 232445)
delete_article(Egor_Moderator, 232445)
delete_article(Nazar_Admin, 234255)
delete_group(Nazar_Admin, 234255)
delete_group(Lena_Member, 22445)
delete_group(Zakhar_Admin, 224456)


