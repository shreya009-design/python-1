// 20. Triangle: A = H * L / 2   (here L = base)
double base, height, area_tri;
printf("Enter base and height of triangle: ");
scanf("%lf %lf", &base, &height);

area_tri = (base * height) / 2.0;

printf("Triangle -> Area = %.2f\n", area_tri);
