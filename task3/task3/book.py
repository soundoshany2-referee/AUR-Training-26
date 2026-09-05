from library_item import LibraryItem, ItemStatus, ITEM_TYPES


class Book(LibraryItem):

    def __init__(self, title, author, isbn):
        super().__init__(title)

        if not LibraryItem.validate_isbn(isbn):
            raise ValueError("Invalid ISBN-13.")

        self.author = author
        self.isbn = isbn

    def loan_period(self):
        return 21

    @classmethod
    def from_dict(cls, data):

        book = cls(
            data["title"],
            data["author"],
            data["isbn"]
        )

        book._status = ItemStatus[data["status"]]

        return book


ITEM_TYPES["Book"] = Book