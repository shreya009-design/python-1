// 17. Square: A = L^2, P = 4L
double side, area_sq, peri_sq;
printf("Enter side of square: ");
scanf("%lf", &side);

area_sq = side * side;
peri_sq = 4 * side;

printf("Square -> Area = %.2f, Perimeter = %.2f\n", area_sq, peri_sq);
