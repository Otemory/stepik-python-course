"""

n = int(input())
for i in range(n):
    print("*" * n)


n = int(input())

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
 """
""" Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. 
Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.

Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке. 
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].

Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a \le ba≤b, c \le dc≤d.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. 
Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы."""

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
a, b, c, d = 7, 10, 5, 6

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    for i in range(a, b +1):
        for j in range(c, d + 1):
            print(i * j, end="\t")
        print()


else:
    print("error")