num1 = int(input("Insert number: "))
operator = input ("Choose operation: - + / *; ")
num2 = int(input("Insert number: "))

while num1 != 0 and num2 != 0:
    if operator == "+":
        print(num1 + num2)
        break

    elif operator == "-":
        print (num1 - num2)
        break

    elif operator == "/":
        print (num1 / num2)
        break

    elif operator == "*":
        print (num1 * num2)
        break

else:
    print("Zero isn`t divide in zero!")
    