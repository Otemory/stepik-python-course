# мое решение
a = int(input())
if 0 <= a <= 1000:
    b = a % 100

    if b < 21:
        if b == 0 or 5 <= b <= 20:
            print(a, "програмистов")
        elif b == 1:
            print(a, "програмист")
        elif 2 <= b <= 4:
            print(a, "програмиста")

    else:
        c = b % 10
        if c == 0 or 5 <= c <= 20:
            print(a, "програмистов")
        elif c == 1:
            print(a, "програмист")
        elif 2 <= c <= 4:
            print(a, "програмиста")

else:
    print("error")
# not mine но улучшеное и дополненное

a = int(input())
a10 = a % 10
a100 = a % 100
if a10 == 1 and a100 != 11:
    print(a, "программист")
elif (a10 in [2, 3, 4]) and (a100 not in [12, 13, 14]):
    print(a, "программиста")
else:
    print(a, "программистов")
