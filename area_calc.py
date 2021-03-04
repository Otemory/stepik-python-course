figure_name = input()
if figure_name == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    if a > 0 and b > 0 and c > 0:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(float(s))
    else:
        print("Wrong")
elif figure_name == "прямоугольник":
    a = int(input())
    b = int(input())
    if a > 0 and b > 0:
        s = a * b
        print(float(s))
    else:
        print("Wrong")
elif figure_name == "круг":
    r = int(input())
    if r > 0:
        s = 3.14 * r ** 2
        print(s)
    else:
        print("Wrong")
else:
    print("Wrong figure")
