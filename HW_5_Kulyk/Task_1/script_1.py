
# Напишіть ітератор який приймає додатнє число n і видає всі числа
# фібоначі від 0 до n (якщо число більше чим n то воно не повертається).
# Добавте метод який перевіряє чи поточний стан ітератора – парне
# число.


class Fib(object):
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        elif fib % 2 == 0:
            self.a, self.b = self.b, self.a + self.b
            return f"{fib} - Pare"
        else:
            self.a, self.b = self.b, self.a + self.b
            return f"{fib} - No Pare"




fib_1 = Fib(256)

for i in fib_1:
    print(i)


