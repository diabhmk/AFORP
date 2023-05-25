#include <stdio.h>
#include <string.h>
#include "books.h"
#include "menu.h"

void searchAuthorByBook() {
    char bookTitle[100];
    printf("Entrez le titre du livre : ");
    scanf("%s", bookTitle);

    char* author = getAuthorByBook(bookTitle);
    if (author != NULL) {
        printf("L'auteur du livre '%s' est : %s\n", bookTitle, author);
    } else {
        printf("Le livre '%s' n'a pas été trouvé dans le répertoire.\n", bookTitle);
    }
    printf("\n");
}

void searchBooksByAuthor() {
    char authorName[100];
    printf("Entrez le nom de l'auteur : ");
    scanf("%s", authorName);

    printf("Les livres écrits par %s sont :\n", authorName);
    int found = 0;
    for (int i = 0; i < bookCount; i++) {
        char* author = getAuthorByBook(bookDirectory[i].title);
        if (author != NULL && strcmp(author, authorName) == 0) {
            printf("- %s\n", bookDirectory[i].title);
            found = 1;
        }
    }

    if (!found) {
        printf("Aucun livre trouvé pour l'auteur '%s'.\n", authorName);
    }
    printf("\n");
}

void searchBooksByPublicationDate() {
    // Ajoutez ici la logique de recherche des livres par date de publication
}

void displayMenu() {
    int choice;
    do {
        printf("=== MENU ===\n");
        printf("1. Rechercher un auteur par son livre\n");
        printf("2. Rechercher un livre par son auteur\n");
        printf("3. Rechercher un livre par sa date de publication\n");
        printf("0. Quitter\n\n");

        printf("Choix : ");
        scanf("%d", &choice);
        printf("\n");

        switch (choice) {
            case 1:
                searchAuthorByBook();
                break;
            case 2:
                searchBooksByAuthor();
                break;
            case 3:
                searchBooksByPublicationDate();
                break;
            case 0:
                printf("Au revoir !\n");
                break;
            default:
                printf("Choix invalide. Veuillez réessayer.\n\n");
                break;
        }
    } while (choice != 0);
}
