#include <stdio.h>

float calcularResistencia() {
    int tipo, N;
    float valor, req = 0;

    printf("El/Los resistor/es estan en serie (ingrese 1) o en paralelo (ingrese 2): ");
    scanf("%d", &tipo);

    printf("Ingrese la cantidad de resistencias: ");
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        printf("Ingrese el valor de la resistencia numero %d: ", i + 1);
        scanf("%f", &valor);

        if (valor <= 0) {
            printf("Error: solo ingresar valores mayores a 0.\n");
            i--;
            continue;
        }

        if (tipo == 1) {
            req += valor;
        } else if (tipo == 2) {
            req+= (1/valor);
        } else {
            printf("Tipo de conexion invalido.\n");
            return -1;
        }
    }

    if (tipo == 2) {
        req = 1 / req;
    }

    return req;
}

int main() {
    printf("--- Calculadora de Resistencias Equivalentes ---\n");

    float resultado = calcularResistencia();

    if (resultado != -1) {
        printf("\nLa resistencia equivalente es: %.2f Ohms\n", resultado);
    }

    return 0;
}
