from models.Book import Book
from models.Library import Library

def main():

    #creating book objects
    book1 = Book("B001","The Prince and the Pauper","Mark twain")
    book2 = Book("B002", "1984", "George Orwell")
    book3 = Book("B003", "To Kill a Mockingbird", "Harper Lee")
    book4 = Book("B004", "The Great Gatsby", "F. Scott Fitzgerald")
    book5 = Book("B005", "The Hobbit", "J.R.R. Tolkien")

    bookList = [book1,book2,book3,book4,book5]

    my_library = Library(bookList)
    
    my_library.displayBooks()

    print("\n")
    print("1 - Borrow Book")
    print("2 - Return Book")

    task = int(input("Enter task number (1/2) : "))

    if task == 1:
       bookId = input("Enter book ID :")
       my_library.borrowBook(bookId)
       print("\n")
       my_library.displayBooks()

    elif task == 2:
        bookId = input("Enter book ID :")
        bookTitle = input("Enter book Title :")
        bookAuthor = input("Enter book Author :")

        new_book = Book(bookId,bookTitle,bookAuthor)
        my_library.returnBook(new_book)
        print("\n")
        my_library.displayBooks()

    else:
        print("Invalid number")


if __name__ == "__main__":
    main()