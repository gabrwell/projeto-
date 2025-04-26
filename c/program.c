#include <stdio.h>


int main(){
    printf("***********************\n");
    printf("*Welcome to the game!*\n");
    printf("***********************\n");

    int numerosecreto;
    numerosecreto = 24;


    int chute;
     
    int tentativas = 1;
    int pontos = 1000;

        while(1) {
        
        printf("Whats your kick: ");
        printf("Attempt %d\n", tentativas);
        scanf("%d", &chute); 
        printf("Your kick is %d ", chute);

        int acertou = (chute == numerosecreto);
        int maior = chute > numerosecreto;

        if (chute < 0 ) {
            printf("Dont put negative numbers!\n");
            
        }

         if (acertou) {
            printf("You win!\n");

          break;
        
            }   else if(maior){
                printf(" The secret number is minor\n");
            } else {
                printf("The secret number is bigger\n");
            }
            printf("You lose\n");
            tentativas++;
                
            }
        

        printf("End game!\n");
        printf("You win in %d attempts!", tentativas);
    }

