# 18. Rectangle: A = L * B, P = 2(L + B)
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

area_rec = length * breadth
peri_rec = 2 * (length + breadth)

print("Rectangle -> Area =", area_rec, "Perimeter =", peri_rec)
