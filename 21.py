// 21. Net salary with 10% allowance and 3% deduction
double gross, allowance, deduction, net_salary;
printf("Enter gross salary: ");
scanf("%lf", &gross);

allowance   = 0.10 * gross;   // 10% of gross
deduction   = 0.03 * gross;   // 3% of gross
net_salary  = gross + allowance - deduction;

printf("Net salary = %.2f\n", net_salary);
