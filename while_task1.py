"""
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке,
и после первого введенного нуля выводит сумму полученных на вход чисел.
"""
a = int(input())
mass = []
while a != 0:
    mass.append(a)
    a = int(input())
print(sum(mass))
###
a = int(input())
summa = 0
while a != 0:
    summa += a
    a = int(input())
print(summa)
