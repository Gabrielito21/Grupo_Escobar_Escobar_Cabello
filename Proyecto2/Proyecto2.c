#include <stdio.h>
#include <stdlib.h> // Para generar valores aleatorios
#include <time.h>  // Para semilla
#include <stdbool.h> // Para utilizar valores booleanos

struct Eslabon { // Se define estructura de eslabón
    int id;
    float x;
    float y;
};

// Función para generar posicion inicial
void generarPosicionInicial(float *posX, float *posY) {
    *posX = (float)(rand() % 361); // Se usa función rand de <stdlib.h> para generar valores aleatorios
    *posY = (float)(rand() % 361);
}

bool simularAutoHome(struct Eslabon *e) {
    while (e->x > 0 || e->y > 0) { // Ciclo while para iterar mientras la posición no sea == 0
        if (e->x > 0) { // Si la posición en x es mayor a 0, se resta 1
            e->x -= 1.0; 
        }
        if (e->y > 0) { // """""""""" en y """"""""""" """"""""""
            e->y -= 1.0;
        }
    }
    
    if (e->x == 0 && e->y == 0) { // Cuando se llega al valor 0, "home" la función retorna "True"
        return true;
    }
    return false;
}

int main() {
    srand(time(NULL)); // Semilla para agregar variabilidad entre ejecuciones 

    struct Eslabon e1, e2, e3, e4; // Se definen structs para cada Eslabón

    e1.id = 1; // Id para Eslabón 1
    e2.id = 2; // Id para Eslabón 2
    e3.id = 3; // Id para Eslabón 3
    e4.id = 4; // Id para Eslabón 4

    generarPosicionInicial(&e1.x, &e1.y); // Se generan posiciones iniciales para cada eslabón
    generarPosicionInicial(&e2.x, &e2.y);
    generarPosicionInicial(&e3.x, &e3.y);
    generarPosicionInicial(&e4.x, &e4.y);

    printf("--- Posiciones Iniciales ---\n"); // Se imprimen las posiciones iniciales de cada eslabón (random)
    printf("Eslabon 1 (X: %.2f, Y: %.2f)\n", e1.x, e1.y);
    printf("Eslabon 2 (X: %.2f, Y: %.2f)\n", e2.x, e2.y);
    printf("Eslabon 3 (X: %.2f, Y: %.2f)\n", e3.x, e3.y);
    printf("Eslabon 4 (X: %.2f, Y: %.2f)\n\n", e4.x, e4.y);

    bool t1, t2, t3, t4;  // Se definen variables booleanas para almacenar el valor booleano que retorna simularAutoHome

    printf("--- Iniciando secuencia Auto-Home ---\n"); // Salida: Se simula el Auto-Home para cada eslabón y se imprime
    // si su ejecución fue exitosa
    t1 = simularAutoHome(&e1);
    if (t1) printf("Eslabon %d terminado\n", e1.id);

    t2 = simularAutoHome(&e2);
    if (t2) printf("Eslabon %d terminado\n", e2.id);

    t3 = simularAutoHome(&e3);
    if (t3) printf("Eslabon %d terminado\n", e3.id);

    t4 = simularAutoHome(&e4);
    if (t4) printf("Eslabon %d terminado\n\n", e4.id);

    if (t1 && t2 && t3 && t4) { // Condicional final que imprime el mensaje solo si todos los eslabones vuelven a 0
        printf("Todos los eslabones realizaron auto-home correctamente.\n");
    }

    return 0;
}