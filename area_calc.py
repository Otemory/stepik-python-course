figure_name = input()
if figure_name == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
elif figure_name == "прямоугольник":
    a = int(input())
    b = int(input())
elif figure_name == "круг":
    r = int(input())
else:
    print("Wrong figure")