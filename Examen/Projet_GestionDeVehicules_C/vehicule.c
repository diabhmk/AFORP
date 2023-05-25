#include <stdio.h>
#include <string.h>
#include "vehicule.h"

struct Vehicule vehicules[100];  // Tableau pour stocker les véhicules
int nombreVehicules = 0;  // Nombre de véhicules enregistrés

void ajouterVehicule() {
    if (nombreVehicules >= 100) {
        printf("La capacité maximale de véhicules est atteinte.\n");
        return;
    }

    printf("Ajout d'un nouveau véhicule :\n");

    struct Vehicule nouveauVehicule;

    printf("Immatriculation: ");
    scanf("%s", nouveauVehicule.immatriculation);

    printf("Marque: ");
    scanf("%s", nouveauVehicule.marque);

    printf("Modèle: ");
    scanf("%s", nouveauVehicule.modele);

    printf("Année: ");
    scanf("%d", &nouveauVehicule.annee);

    printf("Couleur: ");
    scanf("%s", nouveauVehicule.couleur);

    vehicules[nombreVehicules++] = nouveauVehicule;

    printf("Véhicule ajouté avec succès.\n");
}

void supprimerVehicule() {
    if (nombreVehicules == 0) {
        printf("Il n'y a aucun véhicule enregistré.\n");
        return;
    }

    printf("Suppression d'un véhicule :\n");

    char immatriculation[10];
    printf("Immatriculation du véhicule à supprimer: ");
    scanf("%s", immatriculation);

    int i;
    for (i = 0; i < nombreVehicules; i++) {
        if (strcmp(vehicules[i].immatriculation, immatriculation) == 0) {
            int j;
            for (j = i; j < nombreVehicules - 1; j++) {
                vehicules[j] = vehicules[j + 1];
            }
            nombreVehicules--;
            printf("Véhicule supprimé avec succès.\n");
            return;
        }
    }

    printf("Aucun véhicule avec l'immatriculation spécifiée n'a été trouvé.\n");
}

void modifierVehicule() {
    if (nombreVehicules == 0) {
        printf("Il n'y a aucun véhicule enregistré.\n");
        return;
    }

    printf("Modification d'un véhicule :\n");

    char immatriculation[10];
    printf("Immatriculation du véhicule à modifier: ");
    scanf("%s", immatriculation);

    int i;
    for (i = 0; i < nombreVehicules; i++) {
        if (strcmp(vehicules[i].immatriculation, immatriculation) == 0) {
            struct Vehicule vehiculeModifie;

            printf("Nouvelle marque: ");
            scanf("%s", vehiculeModifie.marque);

            printf("Nouveau modèle: ");
            scanf("%s", vehiculeModifie.modele);

            printf("Nouvelle année: ");
            scanf("%d", &vehiculeModifie.annee);

            printf("Nouvelle couleur: ");
            scanf("%s", vehiculeModifie.couleur);

            vehicules[i] = vehiculeModifie;
            printf("Véhicule modifié avec succès.\n");
            return;
        }
    }

    printf("Aucun véhicule avec l'immatriculation spécifiée n'a été trouvé.\n");
}

void afficherListeVehicules() {
    if (nombreVehicules == 0) {
        printf("Il n'y a aucun véhicule enregistré.\n");
        return;
    }

    printf("Liste des véhicules :\n");

    int i;
    for (i = 0; i < nombreVehicules; i++) {
        printf("Véhicule %d:\n", i + 1);
        printf("Immatriculation: %s\n", vehicules[i].immatriculation);
        printf("Marque: %s\n", vehicules[i].marque);
        printf("Modèle: %s\n", vehicules[i].modele);
        printf("Année: %d\n", vehicules[i].annee);
        printf("Couleur: %s\n", vehicules[i].couleur);
        printf("----------------------\n");
    }
}

void rechercherVehicule() {
    if (nombreVehicules == 0) {
        printf("Il n'y a aucun véhicule enregistré.\n");
        return;
    }

    printf("Recherche d'un véhicule :\n");

    char immatriculation[10];
    printf("Immatriculation du véhicule à rechercher: ");
    scanf("%s", immatriculation);

    int i;
    for (i = 0; i < nombreVehicules; i++) {
        if (strcmp(vehicules[i].immatriculation, immatriculation) == 0) {
            printf("Véhicule trouvé :\n");
            printf("Immatriculation: %s\n", vehicules[i].immatriculation);
            printf("Marque: %s\n", vehicules[i].marque);
            printf("Modèle: %s\n", vehicules[i].modele);
            printf("Année: %d\n", vehicules[i].annee);
            printf("Couleur: %s\n", vehicules[i].couleur);
            return;
        }
    }

    printf("Aucun véhicule avec l'immatriculation spécifiée n'a été trouvé.\n");
}

