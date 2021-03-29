'''1729 =1**3+12**3=9**3+10**3
1729 = a ** 3 + b ** 3 = c ** 3 + d ** 3'''
from math import ceil
num = 1729
kub_num = ceil(num ** (1 / 3))
cnt = 0
for a in range(1, 33):
    for b in range(1, 33):
        for c in range (1, 33):
            for d in range (1, 33):
                if a not in (b, c, d) and b not in (a, c, d) and c not in (a, b, d) and d not in (a, b, c):

                     if a ** 3 + b**3  == c**3 + d**3:print(c ** 3 + d ** 3)







