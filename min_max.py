a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(min(a, b, c))

if (b >= a >= c) or (b <= a <= c) or (a == b == c) or (b == a > c) or (b == a < c) or (a == c > b) or (a == c < b):
    print(a)
elif (a >= b >= c) or (a <= b <= c) or (b == c > a):
    print(b)
elif (a >= c >= b) or (a <= c <= b) or (b == c < a):
    print(c)
# ################################################

a = sorted([int(input()), int(input()), int(input())])
print(a[2], a[0], a[1], sep="\n")

# ################################################
a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c), min(a, b, c), ((a + b + c)-(max(a, b, c)+min(a, b, c))), sep="\n")

####################################

a, b, c = int(input()), int(input()), int(input())

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a)
print(b)
print(c)
