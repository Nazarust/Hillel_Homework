#
# list_1 = ["a", "b", "c"]
# try:
#   print("hello" + list_1[5])
# except TypeError:
#   print("type must be integer")

# import math as external_math
#
# print(external_math.pi)

# def func(*args):
#   if len(args) > 5:
#     return True
#   return False
#
# print(func((1, 2, 3, 4, 5, 6, 7), 2, 3))

# def func(*urls):
#   return type(urls)
#
# print(func("https://www.google.com.ua/"))

# try:
#   try:
#     print(1 / 0)
#   except ZeroDivisionError as ex:
#     raise ex
#     print("zero div error")
# except Exception as ex:
#   print("error")


def decor(func):
   def wrap(*args, **kwargs):
      print(args)
      return func(*args, **kwargs)
   return wrap


@decor
def hop(x,y):
    print("woooo")

hop(5,2)