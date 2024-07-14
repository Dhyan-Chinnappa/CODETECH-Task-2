from datetime import datetime, timedelta

class LibraryItem:
    def __init__(self, title, author, category, item_type):
        self.title = title
        self.author = author
        self.category = category
        self.item_type = item_type
        self.is_checked_out = False
        self.due_date = None

class LibrarySystem:
    def __init__(self):
        self.items = []
        self.fines = {}
        self.fine_rate = 0.50  # $0.50 per day overdue

    def add_item(self, title, author, category, item_type):
        item = LibraryItem(title, author, category, item_type)
        self.items.append(item)
        print(f"Item '{title}' added successfully.")

    def check_out_item(self, title, borrower):
        for item in self.items:
            if item.title == title and not item.is_checked_out:
                item.is_checked_out = True
                item.due_date = datetime.now() + timedelta(days=14)  # 2 weeks checkout period
                self.fines[borrower] = self.fines.get(borrower, 0)
                print(f"Item '{title}' checked out by {borrower}. Due date: {item.due_date}.")
                return
        print(f"Item '{title}' is not available for checkout.")

    def return_item(self, title, borrower):
        for item in self.items:
            if item.title == title and item.is_checked_out:
                item.is_checked_out = False
                if datetime.now() > item.due_date:
                    overdue_days = (datetime.now() - item.due_date).days
                    fine = overdue_days * self.fine_rate
                    self.fines[borrower] += fine
                    print(f"Item '{title}' returned late. Fine incurred: ${fine:.2f}")
                else:
                    print(f"Item '{title}' returned on time.")
                item.due_date = None
                return
        print(f"Item '{title}' was not checked out.")

    def search_items(self, title=None, author=None, category=None):
        results = []
        for item in self.items:
            if title and title.lower() not in item.title.lower():
                continue
            if author and author.lower() not in item.author.lower():
                continue
            if category and category.lower() not in item.category.lower():
                continue
            results.append(item)
        
        if results:
            print("Search results:")
            for item in results:
                status = "Checked out" if item.is_checked_out else "Available"
                print(f"Title: {item.title}, Author: {item.author}, Category: {item.category}, Status: {status}")
        else:
            print("No items found matching the search criteria.")

    def view_fines(self, borrower):
        fine = self.fines.get(borrower, 0)
        print(f"Total fines for {borrower}: ${fine:.2f}")

# Example usage:
if __name__ == "__main__":
    library = LibrarySystem()

    # Adding items
    library.add_item("The Great Gatsby", "F. Scott Fitzgerald", "Novel", "Book")
    library.add_item("National Geographic", "Various Authors", "Science", "Magazine")
    library.add_item("Inception", "Christopher Nolan", "Science Fiction", "DVD")

    # Checking out items
    library.check_out_item("The Great Gatsby", "Alice")

    # Returning items
    library.return_item("The Great Gatsby", "Alice")

    # Searching for items
    library.search_items(author="Fitzgerald")

    # Viewing fines
    library.view_fines("Alice")
