#include <stdio.h>

int main()
{
    int temperatura;
    printf("Ingrese un valor entero de temperatura: ");
    scanf("%d",&temperatura);
    
    if ( temperatura < 20) {
        printf ("Estado: Subenfriamiento. \n") ;
    } else if ( temperatura > 45) {
        printf ("Estado: Alarma de Sobrecalentamiento. \n") ;
    } else {
        printf ("Estado: Operación Nominal. \n") ;
    }

    return 0;
}
