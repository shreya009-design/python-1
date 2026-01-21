// 18. Rectangle: A = L * B, P = 2(L + B)
double length, breadth, area_rec, peri_rec;
printf("Enter length and breadth of rectangle: ");
scanf("%lf %lf", &length, &breadth);

area_rec = length * breadth;
peri_rec = 2 * (length + breadth);

printf("Rectangle -> Area = %.2f, Perimeter = %.2f\n", area_rec, peri_rec);
