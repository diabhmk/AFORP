#ifndef BOOKS_H
#define BOOKS_H

typedef struct {
    char title[100];
} Book;

extern Book bookDirectory[];
extern int bookCount;

void populateBookDirectory();
void displayBookDirectory();
char* getAuthorByBook(char* bookTitle);

#endif


