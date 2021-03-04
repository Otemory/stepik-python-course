
a, b, op = float(input("number 1: ")), float(input("number 2: ")), input("operation: ")

if op in ["mod", "pow", "div", "+", "-", "/", "*"]:
    if op in ["div", "/", "mod"] and b == 0:
        print("Деление на 0!")
    else:
        if op == "mod":
            print(a % b)
        elif op == "pow":
            print(a ** b)
        elif op == "div":
            print(a // b)
        elif op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        elif op == "/":
            print(a / b)
else:
    print("wrong operation")
