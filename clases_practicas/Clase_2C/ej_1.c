/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int evaluartemperatura(int temperatura) {

    if (temperatura < 60) {
        printf("normal\n");
        return 0;
    }

    else if (temperatura >= 60 && temperatura <= 85) {
        printf("advertencia\n");
        return 1;
    }

    else if (temperatura > 85) {
        printf("peligro\n");
        return 2;
    }

}

int main() {

    int temperatura;

    for (int i = 1; i <= 5; i++) {

        printf("Ingrese temperatura: ");
        scanf("%d", &temperatura);

        int resultado = evaluartemperatura(temperatura);
    }

    return 0;
}