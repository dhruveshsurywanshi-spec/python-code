# Smart Library Management System
# Using Strings, Lists, Tuples, Sets and Dictionaries

library_info = ("Smart Library", "Computer Science")
book_ids = ["B001", "B002", "B003"]
authors = {"John Smith", "Mark Allen", "Andrew Tanenbaum"}

library = {
    "B001": {"title": "Python Programming",
             "author": "John Smith", "available": True},
    "B002": {"title": "Data Structures",
             "author": "Mark Allen", "available": True},
    "B003": {"title": "Computer Networks",
             "author": "Andrew Tanenbaum", "available": False}
}


def add_book():
    book_id = input("Enter Book ID: ").strip().upper()
    if book_id in library:
        print("Book ID already exists!")
        return
    title = input("Enter Book Title: ").strip().title()
    author = input("Enter Author Name: ").strip().title()
    if not title or not author:
        print("Title and author cannot be empty!")
        return
    library[book_id] = {"title": title,
                        "author": author, "available": True}
    book_ids.append(book_id)
    authors.add(author)
    print("Book added successfully!")


def display_books():
    for book_id, book in library.items():
        status = "Available" if book["available"] else "Issued"
        print(book_id, book["title"], book["author"], status)


def search_book():
    title = input("Enter title to search: ").strip().casefold()
    found = False
    for book_id, book in library.items():
        if title in book["title"].casefold():
            print(book_id, book["title"], book["author"])
            print("Available:", book["available"])
            found = True
    if not found:
        print("Book not found!")


def issue_book():
    book_id = input("Enter Book ID: ").strip().upper()
    if book_id not in library:
        print("Book not found!")
    elif library[book_id]["available"]:
        library[book_id]["available"] = False
        print("Book issued successfully!")
    else:
        print("Book is already issued!")


def return_book():
    book_id = input("Enter Book ID: ").strip().upper()
    if book_id not in library:
        print("Book not found!")
    elif not library[book_id]["available"]:
        library[book_id]["available"] = True
        print("Book returned successfully!")
    else:
        print("Book is already available!")


def count_available():
    count = sum(1 for book in library.values()
                if book["available"])
    print("Available books:", count)


def display_authors():
    print("Unique authors:")
    for author in sorted(authors):
        print(author)


def main():
    while True:
        print("\n--- SMART LIBRARY MANAGEMENT ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Count Available Books")
        print("7. Display Authors")
        print("8. Library Information")
        print("9. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            count_available()
        elif choice == "7":
            display_authors()
        elif choice == "8":
            print("Library:", library_info[0])
            print("Department:", library_info[1])
        elif choice == "9":
            print("Thank you for using the library!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()