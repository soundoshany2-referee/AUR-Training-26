from library_item import LibraryItem


class Database:

    def __init__(self, filename="database.txt"):
        self.filename = filename

    def save(self, items):

        with open(self.filename, "w", encoding="utf-8") as file:

            for item in items:

                data = self.item_to_dict(item)

                line = "|".join(
                    f"{key}={value}"
                    for key, value in data.items()
                )

                file.write(line + "\n")

    def load(self):

        items = []

        with open(self.filename, "r", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                data = {}

                parts = line.split("|")

                for part in parts:

                    key, value = part.split("=", 1)

                    data[key] = value

                item = LibraryItem.from_dict(data)

                items.append(item)

        return items

    def item_to_dict(self, item):

        data = {
            "type": item.__class__.__name__,
            "title": item.title,
        }

        if item.__class__.__name__ == "Book":
            data["author"] = item.author
            data["isbn"] = item.isbn

        elif item.__class__.__name__ == "DVD":
            data["director"] = item.director

        elif item.__class__.__name__ == "Magazine":
            data["issue"] = item.issue

        data["status"] = item.status.value

        return data