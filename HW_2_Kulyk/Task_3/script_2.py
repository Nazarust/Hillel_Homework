
# Task_3 (script_2)

# Реалізуйте алгоритм пошуку n числа фібоначі, циклічним алгоритмом

fib1 = 1
fib2 = 1

n = input("Номер елемента ряда: ")
n = int(n)

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print("Значення:", fib2)
