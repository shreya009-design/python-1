# 21. Net salary = gross + allowance - deduction
# allowance = 10% of gross, deduction = 3% of gross

gross = float(input("Enter gross salary: "))

allowance = 0.10 * gross
deduction = 0.03 * gross
net_salary = gross + allowance - deduction

print("Net salary =", net_salary)
