#include <stdio.h>

int main()
{
    int N;
    int contador = 0;
    
    printf("Ingrese un valor entero postivo limite: ");
    scanf("%d",&N);
    printf("Los numeros pares entre 0 y %d son: ",N);
    for(int i = 0; i<=N; i++) {
        if (i % 2 == 0) {
            printf(" %d ", i);
            contador++; 
        }
    }

    printf("\nNumeros pares detectados: %d\n", contador);

    return 0;
}
