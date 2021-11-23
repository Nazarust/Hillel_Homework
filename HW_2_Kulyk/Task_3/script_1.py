
# Task_3 (script_1)

# Реалізуйте алгоритм пошуку n числа фібоначі, рекурсивним
# алгоритмом

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))

