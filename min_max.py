a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(min(a, b, c))

if (b >= a >= c) or (b <= a <= c) or (a == b == c) or (b == a > c) or (b == a < c) or (a == c > b) or (a == c < b):
    print(a)
elif (a >= b >= c) or (a <= b <= c) or (b == c > a):
    print(b)
elif (a >= c >= b) or (a <= c <= b) or (b == c < a):
    print(c)
