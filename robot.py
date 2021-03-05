
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

