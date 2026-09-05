from library_item import LibraryItem, ItemStatus


class Library:

    def __init__(self):
        self.items = []

    def add_item(self, item):

        if not isinstance(item, LibraryItem):
            raise TypeError("Only LibraryItem objects can be added.")

        self.items.append(item)

    def find_by_title(self, title):

        for item in self.items:

            if item.title.lower() == title.lower():
                return item

        return None

    def checkout(self, title):

        item = self.find_by_title(title)

        if item is None:
            raise ValueError("Item not found.")

        item.checkout()

    def return_item(self, title):

        item = self.find_by_title(title)

        if item is None:
            raise ValueError("Item not found.")

        item.return_item()

    def mark_lost(self, title):

        item = self.find_by_title(title)

        if item is None:
            raise ValueError("Item not found.")

        item.mark_lost()

    def list_available(self):

        available = []

        for item in self.items:

            if item.status == ItemStatus.AVAILABLE:
                available.append(item)

        return available

    def list_all(self):

        return self.items

    def sorted_items(self):

        return sorted(self.items)