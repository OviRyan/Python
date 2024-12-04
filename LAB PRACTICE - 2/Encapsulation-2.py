class LibraryBook:
    def __init__(self, ISBN, title, author):
        self.__ISBN = ISBN
        self._title = title
        self._author = author
        self.status = "available"

    def get_ISBN(self):
        return f"***-{self.__ISBN[-4:]}"

    def borrow_book(self, borrower_name):
        if self.status == "available":
            self.status = "borrowed"
            print(f"{borrower_name} borrowed '{self._title}'. Enjoy reading!")
        else:
            print(f"Oops! '{self._title}' is already borrowed.")

    def _display_basic_info(self):
        print(f"Title: {self._title}, Author: {self._author}")


class DigitalLibraryBook(LibraryBook):
    def __init__(self, ISBN, title, author, file_format):
        super().__init__(ISBN, title, author)
        self.file_format = file_format

    def display_basic_info(self):
        super()._display_basic_info()
        print(f"File format: {self.file_format}")


book1 = LibraryBook("978-3-16-148410-0", "Python for Beginners", "Ov")
print(f"Masked ISBN: {book1.get_ISBN()}")
book1.borrow_book("Shekh")

book2 = DigitalLibraryBook("978-1-23-456789-0", "AI Revolution", "Naf", "PDF")
book2.display_basic_info()
book2.borrow_book("Shekh")
