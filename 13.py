# 13. Convert bytes into KB, MB and GB
bytes_val = float(input("Enter size in bytes: "))
kb = bytes_val / 1024
mb = bytes_val / (1024 ** 2)
gb = bytes_val / (1024 ** 3)
print("KB =", kb)
print("MB =", mb)
print("GB =", gb)
