t_n = input()

a, b, c, d, e, f = int(t_n[0]), int(t_n[1]), int(t_n[2]), int(t_n[3]), int(t_n[4]), int(t_n[5])

start = a + b + c
finish = d + e + f
if start == finish:
    print("Счастливый")
else:
    print("Обычный")
# not mine

nums = [int(i) for i in input()]

print("Счастливый" if sum(nums[:3]) == sum(nums[3:]) else "Обычный")