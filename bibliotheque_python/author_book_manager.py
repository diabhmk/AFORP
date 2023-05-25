class Module3:
    def __init__(self):
        pass

    def get_books_by_author(self, author_name):
        books = {
            "Divers auteurs": ["La Bible", "Le Coran"],
            "Miguel de Cervantes": ["Don Quichotte"],
            "J.K. Rowling": ["Harry Potter à l'école des sorciers"],
            "Antoine de Saint-Exupéry": ["Le Petit Prince"],
            "J.R.R. Tolkien": ["Le Seigneur des Anneaux"],
            "Victor Hugo": ["Les Misérables"],
            "Lewis Carroll": ["Alice au pays des merveilles"],
            "Dan Brown": ["Da Vinci Code"],
            "Mark Twain": ["Les Aventures de Tom Sawyer"],
            "Margaret Mitchell": ["Autant en emporte le vent"],
            "Louisa May Alcott": ["Les Quatre Filles du docteur March"],
            "Alexandre Dumas": ["Le Comte de Monte-Cristo", "Les Trois Mousquetaires"],
            "Jane Austen": ["Orgueil et Préjugés"],
            "Léon Tolstoï": ["Guerre et Paix", "Anna Karenine"],
            "Fiodor Dostoïevski": ["Crime et Châtiment"],
            "Oscar Wilde": ["Le Portrait de Dorian Gray"],
            "Jules Verne": ["Vingt Mille Lieues sous les mers"],
            # Ajoutez ici les 30 autres auteurs avec leurs livres correspondants
        }

        if author_name in books:
            return books[author_name]
        else:
            return None

