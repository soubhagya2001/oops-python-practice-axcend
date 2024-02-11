class Library:
    bookIdStart = 0
    bookList = []

    def __init__(self,title,author,pages):
        Library.bookIdStart +=1
        self.bookId = Library.bookIdStart
        self.title = title
        self.author = author
        self.pages = pages
        Library.bookList.append(self)


    def displayInformation(self):
        print(f"Title : {self.title}\nAuthor : {self.author}\nPages : {self.pages}")


    def removeBooks(self):
        Library.bookList.remove(self)
        print(f"Book removed successfully.")


if __name__ == "__main__":
    while True:
        print("\n\n1.Add Book")
        print("2.Get Book Info")
        print("3.Remove Book")
        print("4.Exit")
        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            title = input("Enter book name : ")
            author = input("Enter author name : ")
            pages = input("Enter book page number :  ")
            book = Library(title,author,pages)
            print(f"Book Added Successfully.\nBook Id NO : {book.bookId}\n\n")

        elif choice == 2:
            bookId = int(input("Enter Book Id : "))
            try:
                book = next((book for book in Library.bookList if book.bookId == bookId))
                if book:
                    book.displayInformation()
                
            except:
                print("No Book found.")

        elif choice == 3:
            bookId = int(input("Enter Book Id : "))
            book = next((book for book in Library.bookList if book.bookId == bookId))
            if book:
                book.removeBooks()

        elif choice == 4:
            break

        else:
            print("Invalid choice! Please enter a valid option (1-3).")
