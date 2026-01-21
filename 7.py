# 7. Convert minutes into hours
mins = int(input("\nEnter time in minutes: "))
h = mins // 60          # whole hours
m = mins % 60           # remaining minutes
print("Hours =", h, "Minutes =", m)
