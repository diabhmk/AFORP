#include <stdio.h>
#include <string.h>
#include "books.h"

#define MAX_BOOKS 50

Book bookDirectory[MAX_BOOKS];
int bookCount = 0;

void populateBookDirectory() {
    strcpy(bookDirectory[bookCount].title, "La Bible");
    bookCount++;
    // Ajoutez ici les 49 autres titres de livres
}

void displayBookDirectory() {
    printf("Répertoire des livres :\n");
    for (int i = 0; i < bookCount; i++) {
        printf("Titre: %s\n", bookDirectory[i].title);
    }
    printf("\n");
}

char* getAuthorByBook(char* bookTitle) {
    if (strcmp(bookTitle, "La Bible") == 0) {
        return "Divers auteurs";
    }
    // Ajoutez ici les 49 autres titres de livres avec leurs auteurs correspondants
    return NULL;
}
