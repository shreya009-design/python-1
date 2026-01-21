# 5. Add, multiply, subtract and divide two numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction (a - b) =", a - b)
print("Multiplication =", a * b)
if b != 0:
    print("Division (a / b) =", a / b)
else:
    print("Division not possible (b is 0)")
