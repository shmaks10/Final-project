class books():
    def __init__(self):
        self.author = "Max"
        self.title = ""
        self.price = 0
        self.Books = {}

    def add(self):
        self.title = input("Enter the name of the book you would like to add:\n").upper()
        self.author = input ("Enter the Author of the book you have just added:\n").upper()
        self.price = float(input("Enter the lsting price of the book:\n"))
        self.Books[self.title] = {'Author': self.author, 'Price':self.price}
        print(self.Books[self.title])
    
    def sell(self):
        while (True):
            self.title = input("What book do you like to sell a book?\n")
            if self.title in self.Books:
                del self.Books[self.title]    
                break
            else:
                print ("Your book wan't found. Try again")
    def showbook(self):
        for x in self.Books:
            print("\n",x)
            print("\n",self.Books[x]['Author'])
            print("\n",self.Books[x]['Price'])
    def savebook(self):
        name = input("Enter the name of the file")
        file = open(name, "x")
        file.write