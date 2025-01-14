class Book:
    def __init__(self, title, pages, price, completed):
        self.title = title
        self.pages = pages
        self.price = price
        self.completed = completed


Book1 = Book("heli hogu karana", 200, 150.50, True)
Book2 = Book(title= "Chomana dudi",pages=100,price= 95.40,completed= True)


print(Book2.completed)
print(Book1)  # prints the address of the object where it is stored