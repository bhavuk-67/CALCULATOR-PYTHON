# Simple Calculator with Further Calculations

result = 0

while True:

    num = float(input("Enter number: "))
    op = input("Enter operator (+, -, *, /): ")

    if result == 0:
        result = num

    if op == "+":
        next_num = float(input("Enter next number: "))
        result = result + next_num

    elif op == "-":
        next_num = float(input("Enter next number: "))
        result = result - next_num

    elif op == "*":
        next_num = float(input("Enter next number: "))
        result = result * next_num

    elif op == "/":
        next_num = float(input("Enter next number: "))

        if next_num != 0:
            result = result / next_num
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid operator")

    print("Current Result =", result)

    choice = input("Do more calculations? (yes/no): ")

    if choice == "no":
        break