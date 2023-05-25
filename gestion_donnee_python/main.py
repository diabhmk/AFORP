from module1 import Module1
from module2 import Module2
from module3 import Module3
from module4 import Module4

class Main:
    def __init__(self):
        self.module1 = Module1()
        self.module2 = Module2()
        self.module3 = Module3()
        self.module4 = Module4()
        self.book_directory = []

    def run(self):
        self.display_welcome_message()
        self.populate_book_directory()
        self.display_book_directory()
        self.display_menu()

    def display_welcome_message(self):
        print("Bienvenue dans la bibliothèque de l'AFORP")
        print()

    def populate_book_directory(self):
        book_titles = [
            "La Bible", "Le Coran", "Don Quichotte", "Harry Potter à l'école des sorciers",
            "Le Petit Prince", "Le Seigneur des Anneaux", "Les Misérables", "Alice au pays des merveilles",
            "Da Vinci Code", "Les Aventures de Tom Sawyer", "Autant en emporte le vent",
            "Les Quatre Filles du docteur March", "Le Comte de Monte-Cristo", "Orgueil et Préjugés",
            "Guerre et Paix", "Crime et Châtiment", "Anna Karenine", "Le Portrait de Dorian Gray",
            "Vingt Mille Lieues sous les mers", "Les Trois Mousquetaires",
            # Ajoutez ici les 30 autres titres de livres
        ]

        for title in book_titles:
            book = self.module1.create_book(title)
            self.book_directory.append(book)

    def display_book_directory(self):
        print("Répertoire des livres :")
        for book in self.book_directory:
            print(f"Titre: {book['Titre']}")
        print()

    def display_menu(self):
        while True:
            print("=== MENU ===")
            print("1. Rechercher un auteur par son livre")
            print("2. Rechercher un livre par son auteur")
            print("3. Rechercher un livre par sa date de publication")
            print("0. Quitter")
            print()

            choice = input("Choix : ")
            if choice == "1":
                self.search_author_by_book()
            elif choice == "2":
                self.search_books_by_author()
            elif choice == "3":
                self.search_books_by_publication_date()
            elif choice == "0":
                print("Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
                print()

    def search_author_by_book(self):
        book_title = input("Entrez le titre du livre : ")
        author = self.module2.get_author_by_book(book_title)
        if author:
            print(f"L'auteur du livre '{book_title}' est : {author}")
        else:
            print(f"Le livre '{book_title}' n'a pas été trouvé dans le répertoire.")
        print()

    def search_books_by_author(self):
        author_name = input("Entrez le nom de l'auteur : ")
        books = self.module3.get_books_by_author(author_name)
        if books:
            print(f"Les livres écrits par {author_name} sont :")
            for book in books:
                print(f"- {book}")
        else:
            print(f"Aucun livre trouvé pour l'auteur '{author_name}'.")
        print()

    def search_books_by_publication_date(self):
        publication_date = input("Entrez la date de publication : ")
        books = self.module4.get_books_by_publication_date(publication_date)
        if books:
            print(f"Les livres publiés en {publication_date} sont :")
            for book in books:
                print(f"- {book}")
        else:
            print(f"Aucun livre trouvé pour la date de publication '{publication_date}'.")
        print()

if __name__ == "__main__":
    app = Main()
    app.run()
