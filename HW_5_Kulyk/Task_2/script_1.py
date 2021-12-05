
# Напишіть генератор який приймає число d (фіксована різниця між
# членами арифметичної прогресії) і кожним викликом next даний
# генератор повертає наступний член арифметичної прогресії

def pr(first_el, d):
    el = first_el - d
    while True:
        el += d
        yield el


ar_pr = pr(5, 5)
print(next(ar_pr))
print(next(ar_pr))
print(next(ar_pr))
print(next(ar_pr))
