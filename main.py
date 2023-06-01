class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        print(f"name: {self.title}")
        print(f"avtor: {self.author}")
book1 = Book("hari poter", "dzhoan royling")
book1.get_info()
book2 = Book("hobbit", "Джон Рональд Руэл Толкин")
book2.get_info()
