'''
a = 5
while a <= 55:
    print(a)
    a += 2

a = 5
while a <= 55:
    if a % 2 == 1:
        print(a)
    a += 1
'''
'''
i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
        print(i)
'''
'''
b = int(input())
a = "*"
c = 1
while c <= b:
    print(a * c)
    c += 1

#####
n = int(input())
star = "*"
while len(star) <= n:
    print(star)
    star += "*"
'''
a, b = int(input()), int(input())
summa = 0
peremennaya = a
while peremennaya <= b:
    summa += peremennaya
    peremennaya += 1
print(summa)