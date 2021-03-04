figure_name = input()
if figure_name == "треугольник":
    a, b, c = float(input()), float(input()), float(input())
    if a > 0 and b > 0 and c > 0:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        # print(float(s))
    else:
        print("Wrong")
elif figure_name == "прямоугольник":
    a, b = float(input()), float(input())
    if a > 0 and b > 0:
        s = a * b
        # print(float(s))
    else:
        print("Wrong")
elif figure_name == "круг":
    r = float(input())
    if r > 0:
        s = 3.14 * r ** 2
        # print(float(s))
    else:
        print("Wrong")
else:
    print("Wrong figure")
print(s)
