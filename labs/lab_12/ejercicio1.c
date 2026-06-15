/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdio.h>

typedef struct {
    int id;
    float nivel_actual;
    float capacidad_maxima;
    int valvula_abierta; // 0 = cerrada, 1 = abierta
} Estanque;

void Estanque_init(Estanque* self, int id_asignado, float cap_max) {
    self->id = id_asignado;
    self->nivel_actual = 0.0;
    self->capacidad_maxima = cap_max;
    self->valvula_abierta = 0;
}

void Estanque_llenar(Estanque* self, float litros) {

    if (self->nivel_actual + litros > self->capacidad_maxima) {

        printf("ALERTA DE SEGURIDAD: capacidad maxima excedida.\n");
        printf("Inyeccion rechazada.\n");

        self->valvula_abierta = 0;

    } else {

        self->valvula_abierta = 1;

        self->nivel_actual = self->nivel_actual + litros;

        printf("Llenado exitoso.\n");
        printf("Nivel actual: %.2f litros\n", self->nivel_actual);

        self->valvula_abierta = 0;
    }
}

int main() {

    Estanque tanque;

    Estanque_init(&tanque, 1, 100.0);

    Estanque_llenar(&tanque, 32.1);
    Estanque_llenar(&tanque, 47.7);
    Estanque_llenar(&tanque, 32.1);

    return 0;
}
