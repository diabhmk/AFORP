#ifndef JEU_H
#define JEU_H

#include "personnage.h"

int genererCoupAleatoire();
void afficherChoix();
int determinerGagnant(int coupJoueur, int coupAdversaire);
void afficherResultat(int resultat);
int jouerPartie(Personnage* joueur);
void afficherPoints(Personnage* joueur);

#endif
