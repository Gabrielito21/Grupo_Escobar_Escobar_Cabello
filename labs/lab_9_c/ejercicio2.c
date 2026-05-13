/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main() {
    int num1, num2;
    
    printf("ingresa el primer número entero: ");
    scanf("%d", &num1);
    printf("ingrese el segundo número entero: ");
    scanf("%d", &num2);

    
    printf("Suma: %d\n", num1 + num2);
    printf("Resta: %d\n", num1 - num2);
    printf("Multiplicación: %d\n", num1 * num2);
    printf("División (entera): %d\n", num1 / num2); 
    printf("Módulo (resto): %d\n", num1 % num2); 

    return 0;
}