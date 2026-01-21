# 16. Calculate interest where I = PRN / 100
p = float(input("Enter principal (P): "))
r = float(input("Enter rate (R): "))
n = float(input("Enter time (N): "))
interest = p * r * n / 100
print("Interest =", interest)
