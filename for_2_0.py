a, b = input().split()
a = int(a)
b = int(b)
summa = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        summa += i
print(summa)
