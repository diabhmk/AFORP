#ifndef VEHICULE_H
#define VEHICULE_H

struct Vehicule {
    char immatriculation[10];
    char marque[20];
    char modele[20];
    int annee;
    char couleur[20];
};

void ajouterVehicule();
void supprimerVehicule();
void modifierVehicule();
void afficherListeVehicules();
void rechercherVehicule(); 

#endif  // VEHICULE_H


