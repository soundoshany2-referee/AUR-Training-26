from library_item import LibraryItem, ItemStatus, ITEM_TYPES


class Magazine(LibraryItem):

    def __init__(self, title, issue):
        super().__init__(title)

        self.issue = issue

    def loan_period(self):
        return 14

    @classmethod
    def from_dict(cls, data):

        magazine = cls(
            data["title"],
            data["issue"]
        )

        magazine._status = ItemStatus[data["status"]]

        return magazine


ITEM_TYPES["Magazine"] = Magazine