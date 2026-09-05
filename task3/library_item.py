from abc import ABC, abstractmethod
from enum import Enum


class ItemStatus(Enum):
    AVAILABLE = "AVAILABLE"
    CHECKED_OUT = "CHECKED_OUT"
    LOST = "LOST"


class LibraryItem(ABC):

    def __init__(self, title):
        self.title = title
        self._status = ItemStatus.AVAILABLE

    @property
    def status(self):
        return self._status

    def checkout(self):
        if self._status != ItemStatus.AVAILABLE:
            raise ValueError("Item is not available.")

        self._status = ItemStatus.CHECKED_OUT

    def return_item(self):
        if self._status != ItemStatus.CHECKED_OUT:
            raise ValueError("Item is not checked out.")

        self._status = ItemStatus.AVAILABLE

    def mark_lost(self):
        if self._status == ItemStatus.LOST:
            raise ValueError("Item is already lost.")

        self._status = ItemStatus.LOST

    @abstractmethod
    def loan_period(self):
        pass

    def __lt__(self, other):
        if not isinstance(other, LibraryItem):
            return NotImplemented

        return self.title.lower() < other.title.lower()

    def __str__(self):
        return f"{self.title} ({self.__class__.__name__}) — {self.status.value}"

    def __repr__(self):
        return f"{self.__class__.__name__}(title={self.title!r})"

    @staticmethod
    def validate_isbn(isbn):
        """
        Validates ISBN-13.
        """

        isbn = isbn.replace("-", "").replace(" ", "")

        if len(isbn) != 13 or not isbn.isdigit():
            return False

        total = 0

        for i in range(12):
            if i % 2 == 0:
                total += int(isbn[i])
            else:
                total += int(isbn[i]) * 3

        check_digit = (10 - (total % 10)) % 10

        return check_digit == int(isbn[12])

    @classmethod
    def from_dict(cls, data):
        item_type = data["type"]

        item_class = ITEM_TYPES[item_type]

        return item_class.from_dict(data)



