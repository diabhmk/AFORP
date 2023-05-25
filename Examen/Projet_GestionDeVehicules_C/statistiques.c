#include <stdio.h>
#include "vehicule.h"
#include "statistiques.h"

extern int nombreVehicules;

void afficherStatistiques() {
    if (nombreVehicules == 0) {
        printf("Il n'y a aucun véhicule enregistré.\n");
        return;
    }

    printf("Statistiques :\n");
    printf("Nombre total de véhicules: %d\n", nombreVehicules);
    printf("----------------------\n");

    
}

