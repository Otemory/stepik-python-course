"""

a, b = input().split()
a = int(a)
b = int(b)
summa = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        summa += i
print(summa)
#############

a, b = input().split()
a = int(a)
b = int(b)
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    s += i
print(s)
#########
a, b = (int(i) for i in input(). split())
print(a, "***", b)
"""

"""Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль 
среднее арифметическое всех чисел из отрезка [a; b][a;b], которые кратны числу 3.

В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [-5; 12]. 
Всего чисел, делящихся на 3, на этом отрезке 6: -3, 0, 3, 6, 9, 12. Их среднее арифметическое равно 4.5

На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3"""
"""
# a, b = (int(i) for i in input().split())
a = int(input())
b = int(input())

avg = []
if a % 3 == 0 or b % 3 == 0:
    while a % 3 != 0:
        a += 1
    for i in range(a, b + 1, 3):
        avg.append(i)
    print(sum(avg) / len(avg))

else:
    print("Error")

######## только математика
a,b = int(input()), int(input())
a += -a % 3
b -= b % 3
print((a+b) / 2)
"""
###### без массива
a, b = int(input()), int(input())

sm = 0
n = 0
j = a
while j % 3 != 0:
    j += 1
for i in range(j, b + 1, 3):
    sm += i
    n += 1

print(sm / n)
