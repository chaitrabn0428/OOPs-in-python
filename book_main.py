class Book:
    def __init__(self, title, pages, price, completed):
        self.title = title
        self.pages = pages
        self.price = price
        self.completed = completed

    def reading(self):
        print("I started reading this book")

    def done(self):
        print("Completed reading this book", self.title)

    def details(self):
        print(f"{self.title}, {self.pages}, {self.price}, {self.completed}")

        