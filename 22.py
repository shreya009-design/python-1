# 22. Net sales = gross sales - 10% discount

gross_sales = float(input("Enter gross sales: "))

discount = 0.10 * gross_sales
net_sales = gross_sales - discount      # or gross_sales * 0.90

print("Net sales =", net_sales)
