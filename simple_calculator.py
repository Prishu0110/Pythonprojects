x = input("Enter the First number: ")
y = input("Enter the Second number: ")

# Valid operators
operators = {"+", "-", "*", "/", "%"}

print("Operators:")
print("+")
print("-")
print("*")
print("/")
print("%")

operator = input("Enter the operator: ")

if operator in operators:
    if operator == "+":
        print(int(x) + int(y))
    elif operator == "-":
        print(int(x) - int(y))
    elif operator == "*":
        print(int(x) * int(y))
    elif operator == "/":
        if int(y) != 0:
            print(int(x) / int(y))
        else:
            print("Cannot divide by zero")
    elif operator == "%":
        print(int(x) % int(y))
else:
    print("Invalid operator")
