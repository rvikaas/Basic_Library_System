class Book:
    def __init__(self,bookId,title,author):
        self.bookId = bookId
        self.title = title
        self.author = author

    def displayBook(self):
        print(f"{self.title} by {self.author}")