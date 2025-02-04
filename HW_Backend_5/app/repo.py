class BooksRepository:
    def __init__(self):
        self.books = [
            {
                "id": 1,
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "year": 1960,
                "total_pages": 336,
                "genre": "Fiction",
            },
            {
                "id": 2,
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "total_pages": 328,
                "genre": "Dystopian",
            },
            {
                "id": 3,
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "year": 1925,
                "total_pages": 180,
                "genre": "Classic",
            },
            {
                "id": 4,
                "title": "The Lord of the Rings",
                "author": "J.R.R. Tolkien",
                "year": 1954,
                "total_pages": 1178,
                "genre": "Fantasy",
            },
            {
                "id": 5,
                "title": "The Catcher in the Rye",
                "author": "J.D. Salinger",
                "year": 1951,
                "total_pages": 224,
                "genre": "Coming-of-age",
            },
        ]

    def get_all(self):
        return self.books

    def get_one(self, book_id: int):
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None

    def save(self, book):
        self.books.append(book)
        return book

    def update(self, book_id: int, updated_data: dict):
        for book in self.books:
            if book["id"] == book_id:
                book.update(updated_data)
                return book
        return None

    def delete(self, book_id: int):
        for index, book in enumerate(self.books):
            if book["id"] == book_id:
                return self.books.pop(index)
        return None