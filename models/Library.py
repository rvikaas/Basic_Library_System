class Library:
    def __init__(self,books):
        self.books = books
    
    #borrow a book
    def borrowBook(self,BookId):
        for book in self.books:
            if BookId == book.bookId:
                self.books.remove(book)
                print(f"You borrowed book : {book.title}")
                break


    #return a book
    def returnBook(self,Book):
        for book in self.books:
            if Book.bookId == book.bookId:
                print(f"Book is already in the Library")
                return

        self.books.append(Book)
        print(f"You returned book : {Book.title}")

    
    #display all books
    def displayBooks(self):
        print("----------Available books----------")
        for book in self.books:
            book.displayBook()