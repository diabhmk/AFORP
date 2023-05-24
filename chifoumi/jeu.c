#include <stdio.h>
#include <stdlib.h>
#include "personnage.h"
#include "jeu.h"

enum Coup { PIERRE, FEUILLE, CISEAUX };

int genererCoupAleatoire() {
    return rand() % 3;  // Génère un nombre aléatoire entre 0 et 2
}

void afficherChoix() {
    printf("1. Pierre\n");
    printf("2. Feuille\n");
    printf("3. Ciseaux\n");
}

int determinerGagnant(int coupJoueur, int coupAdversaire) {
    if (coupJoueur == coupAdversaire) {
        return 0;  // Égalité
    }
    else if ((coupJoueur == PIERRE && coupAdversaire == CISEAUX) ||
             (coupJoueur == FEUILLE && coupAdversaire == PIERRE) ||
             (coupJoueur == CISEAUX && coupAdversaire == FEUILLE)) {
        return 1;  // Joueur gagne
    }
    else {
        return -1;  // Adversaire gagne
    }
}

void afficherResultat(int resultat) {
    if (resultat == 1) {
        printf("Vous gagnez ce tour !\n");
    }
    else if (resultat == -1) {
        printf("Vous perdez ce tour !\n");
    }
    else {
        printf("Égalité !\n");
    }
}

int jouerPartie(Personnage* joueur) {
    int choix;
    int coupJoueur, coupAdversaire;

    for (int tour = 1; tour <= 3; tour++) {
        printf("\nTour %d\n", tour);
        printf("Choisissez votre coup :\n");
        afficherChoix();
        printf("Votre choix (1-3) : ");
        scanf("%d", &choix);

        coupJoueur = choix - 1;
        coupAdversaire = genererCoupAleatoire();

        printf("Vous avez choisi : ");
        switch (coupJoueur) {
            case PIERRE:
                printf("Pierre\n");
                break;
            case FEUILLE:
                printf("Feuille\n");
                break;
            case CISEAUX:
                printf("Ciseaux\n");
                break;
            default:
                printf("Choix invalide\n");
                tour--;  // Réduit le nombre de tours si choix invalide
                continue;
        }

        printf("L'adversaire a choisi : ");
        switch (coupAdversaire) {
            case PIERRE:
                printf("Pierre\n");
                break;
            case FEUILLE:
                printf("Feuille\n");
                break;
            case CISEAUX:
                printf("Ciseaux\n");
                break;
        }

        int resultat = determinerGagnant(coupJoueur, coupAdversaire);
        if (resultat == 1) {
            printf("Vous gagnez ce tour !\n");
            joueur->points++;
        }
        else if (resultat == -1) {
            printf("Vous perdez ce tour !\n");
        }
        else {
            printf("Égalité !\n");
        }
    }

    if (joueur->points == 3) {
        printf("\nFélicitations, vous avez remporté la partie !\n");
    }

    return joueur->points;
}

void afficherPoints(Personnage* joueur) {
    printf("Points du joueur : %d\n", joueur->points);
}
