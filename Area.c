#include<stdio.h>
#include<conio.h>
void main(){
        float radio , area ;
        area=0;
        radio=0;


        printf("Area de circulo \n");
        //entrada de datos
        printf("\nIntroduce el radio=> ");
        scanf("%f",&radio);
        /*Proceso para calcular  el area total*/
        if(area==0||radio==0){
            if(radio == 1 || area ==3)
            {
            }
            else
            {
                for(i = 0; i<2 ; i++)
                {
                    print("Que afortunado\n")
                }
            }

        }

        area=3.1416*pow(radio,2);
        //salida
        printf("\n\nArea=%5.2f",area);
        getch();
        }