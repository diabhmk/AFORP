class Module2:
    def __init__(self):
        pass

    def get_author_by_book(self, book_title):
        authors = {
            "La Bible": "Divers auteurs",
            "Le Coran": "Divers auteurs",
            "Don Quichotte": "Miguel de Cervantes",
            "Harry Potter à l'école des sorciers": "J.K. Rowling",
            "Le Petit Prince": "Antoine de Saint-Exupéry",
            "Le Seigneur des Anneaux": "J.R.R. Tolkien",
            "Les Misérables": "Victor Hugo",
            "Alice au pays des merveilles": "Lewis Carroll",
            "Da Vinci Code": "Dan Brown",
            "Les Aventures de Tom Sawyer": "Mark Twain",
            "Autant en emporte le vent": "Margaret Mitchell",
            "Les Quatre Filles du docteur March": "Louisa May Alcott",
            "Le Comte de Monte-Cristo": "Alexandre Dumas",
            "Orgueil et Préjugés": "Jane Austen",
            "Guerre et Paix": "Léon Tolstoï",
            "Crime et Châtiment": "Fiodor Dostoïevski",
            "Anna Karenine": "Léon Tolstoï",
            "Le Portrait de Dorian Gray": "Oscar Wilde",
            "Vingt Mille Lieues sous les mers": "Jules Verne",
            "Les Trois Mousquetaires": "Alexandre Dumas",
            # Ajoutez ici les 30 autres livres avec leurs auteurs correspondants
        }

        if book_title in authors:
            return authors[book_title]
        else:
            return None

