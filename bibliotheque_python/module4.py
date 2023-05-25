class Module4:
    def __init__(self):
        pass

    def get_books_by_publication_date(self, publication_date):
        books = {
            # Ajoutez ici les dates de publication des livres avec la liste des titres correspondants
        }

        if publication_date in books:
            return books[publication_date]
        else:
            return None
