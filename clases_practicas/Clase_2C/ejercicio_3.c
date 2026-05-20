/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

void generarRampaPWM(int velocidadInicial, int velocidadFinal, int paso) {

    int porcentaje;
    if (velocidadInicial<=velocidadFinal && paso>0) {
        while (velocidadInicial <= velocidadFinal) {

            porcentaje = (velocidadInicial * 100) / velocidadFinal;

            printf("La velocidad esta en %d%%\n", porcentaje);

            velocidadInicial += paso;
        }
    }
    else 
    printf("ERROR NIGGA YOU GAY");
}

int main() {

    int velocidadInicial, velocidadFinal, paso;

    printf("Ingrese velocidad inicial: ");
    scanf("%d", &velocidadInicial);

    printf("Ingrese velocidad final: ");
    scanf("%d", &velocidadFinal);

    printf("Ingrese el paso de la velocidad: ");
    scanf("%d", &paso);

    generarRampaPWM(velocidadInicial, velocidadFinal, paso);

    return 0;
}