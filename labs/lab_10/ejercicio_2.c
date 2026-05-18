/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby,
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main(){
    int numero ;
	do {

		printf("opcion 1: Activar motor \n");
		printf("opcion 2: Apagar motor \n");
		printf("opcion 3: leer estado \n");
		printf("opcion 4: salir nigga \n\n");
		printf("ingrese numero :\n");
		scanf ("%d", & numero ) ;
		
		switch(numero){
			case 1:
		    printf("activando motor \n");
		    break;
	    case 2:
		    printf("apagando motor \n");
		    break;
    	case 3:
		    printf("leyendo estado \n");
		    break;
	    default:
		    printf("opcion invalida \n");
	}
	}while(numero!= 4);
		return 0;
	}
