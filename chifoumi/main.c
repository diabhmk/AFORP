#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "personnage.h"
#include "jeu.h"

int main() {
    srand(time(NULL));
    Personnage joueur;

    printf("Création du personnage\n");
    printf("Entrez le nom de votre personnage : ");
    scanf("%s", joueur.nom);

    joueur.points = 0;

    printf("\nBienvenue, %s !\n", joueur.nom);

    int choix;
    int continuer = 1;

    do {
        int resultat = jouerPartie(&joueur);
        afficherResultat(resultat);
        afficherPoints(&joueur);

        if (joueur.points < 3) {
            printf("\nSouhaitez-vous jouer à nouveau ?\n");
            printf("1. Rejouer\n");
            printf("2. Quitter\n");
            printf("Votre choix : ");
            scanf("%d", &choix);

            if (choix != 1) {
                continuer = 0; // Quitter le jeu
            }
        } else {
            continuer = 0; // Quitter le jeu si le joueur a gagné
        }

    } while (continuer);

    return 0;
}
