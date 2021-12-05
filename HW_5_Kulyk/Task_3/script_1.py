
# Напишіть корутину яка через метод send() отримує певне число, а
# повертає середнє арифметичне чисел що були отримані раніше
# (включаючи те що отримали)

def average():
    sum_ = 0
    amount = 0
    a = 0
    while True:
        a = yield (sum_ + a) / (amount + 1)
        print((sum_ + a) / (amount + 1))
        sum_ += a
        amount += 1
