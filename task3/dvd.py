from library_item import LibraryItem, ItemStatus, ITEM_TYPES


class DVD(LibraryItem):

    def __init__(self, title, director):
        super().__init__(title)

        self.director = director

    def loan_period(self):
        return 5

    @classmethod
    def from_dict(cls, data):

        dvd = cls(
            data["title"],
            data["director"]
        )

        dvd._status = ItemStatus[data["status"]]

        return dvd


ITEM_TYPES["DVD"] = DVD