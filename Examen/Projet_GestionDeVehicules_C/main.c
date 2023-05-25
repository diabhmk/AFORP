#include <stdio.h>
#include <stdlib.h>
#include "vehicule.h"
#include "statistiques.h"

void afficherMenu() {
    printf("=== Gestion des Véhicules ===\n");
    printf("1. Ajouter un véhicule\n");
    printf("2. Supprimer un véhicule\n");
    printf("3. Modifier un véhicule\n");
    printf("4. Afficher la liste des véhicules\n");
    printf("5. Rechercher un véhicule\n");
    printf("6. Afficher les statistiques\n");
    printf("0. Quitter\n");
    printf("Choix : ");
}

int main() {
    int choix = -1;

    while (choix != 0) {
        afficherMenu();
        scanf("%d", &choix);

        switch (choix) {
            case 1:
                ajouterVehicule();
                break;
            case 2:
                supprimerVehicule();
                break;
            case 3:
                modifierVehicule();
                break;
            case 4:
                afficherStatistiques();
                break;
            case 5:
                afficherListeVehicules();
                break;
            case 6:
                rechercherVehicule();
                break;
            case 0:
                printf("Merci d'avoir utilisé l'application. Au revoir!\n");
                break;
            default:
                printf("Choix invalide. Veuillez choisir une option valide.\n");
                break;
        }
    } while (choix != 0);

    return 0;
}
