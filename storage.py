class books():
    def __init__(self):
        self.author = "Max"
        self.title = ""
        self.price = 0
        self.Books = {}

    def add(self):
        self.title = input("Enter the name of the book you would like to add:\n")
        self.author = input ("Enter the Author of the book you have just added:\n")
        self.price = float(input("Enter the lsting price of the book:\n"))
        self.Books[self.title] = {'Author': self.author, 'Price':self.price}
        print(self.Books[self.title])