#include <stdio.h>
#include <stdlib.h>
#include "welcome.h"
#include "books.h"
#include "menu.h"

int main() {
    displayWelcomeMessage();
    populateBookDirectory();
    displayBookDirectory();
    displayMenu();

    return 0;
}

