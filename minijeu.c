#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int nombreMystere, nombreJoueur, essais = 0;
    srand(time(NULL));
    nombreMystere = rand() % 100 + 1;  // Génère un nombre aléatoire entre 1 et 100
    
    printf("=== Devinez le nombre mystère (entre 1 et 100) ===\n");
    
    do {
        printf("Entrez un nombre : ");
        scanf("%d", &nombreJoueur);
        essais++;
        
        if (nombreJoueur < nombreMystere) {
            printf("C'est plus !\n");
        } else if (nombreJoueur > nombreMystere) {
            printf("C'est moins !\n");
        } else {
            printf("Bravo, vous avez trouvé le nombre mystère en %d essais !\n", essais);
        }
        
    } while (nombreJoueur != nombreMystere);
    
    return 0;
}
