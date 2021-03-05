ticket_number = input()
spisok = list(ticket_number)

a, b, c, d, e, f = int(ticket_number[0]), int(ticket_number[1]), int(ticket_number[2]), int(ticket_number[3]), int(ticket_number[4]), int(ticket_number[5])
start = a + b + c
finish = d + e + f
if start == finish:
    print("Счастливый")
else:
    print("Обычный")
'''
print(a + b + c)
print(d + e + f)


a = int(ticket_number[0:3])
b = int(ticket_number[3:])
print(a)
print(b)
'''