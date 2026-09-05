from library import Library
from database import Database
from book import Book
from dvd import DVD
from magazine import Magazine


def main():

    library = Library()
    database = Database()

    
    try:
        items = database.load()

        for item in items:
            library.add_item(item)

        print("Items loaded successfully.\n")

    except FileNotFoundError:
        print("database.txt not found. Starting with empty library.\n")

    
    print("All items:")

    for item in library.sorted_items():
        print(item)

    print("\nAvailable items:")

    for item in library.list_available():
        print(item)

    
    print("\nChecking out Dune...")

    try:
        library.checkout("Dune")
        print("Dune checked out successfully.")

    except ValueError as error:
        print("Error:", error)

    
    dune = library.find_by_title("Dune")

    if dune:
        print("\nDune status:")
        print(dune)

        print("Loan period:", dune.loan_period(), "days")

    
    print("\nReturning Dune...")

    try:
        library.return_item("Dune")
        print("Dune returned successfully.")

    except ValueError as error:
        print("Error:", error)

    
    database.save(library.items)

    print("\nLibrary saved successfully.")


