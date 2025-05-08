class books():
    def __init__(self):
        self.author = ""
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
            self.Books[x]['Price'] = str(self.Books[x]['Price'])
            content1 = str(x +"\n" + self.Books[x]['Author'] + "\n" + self.Books[x]['Price'])
            print(content1)
            #print("\n",x)
            #print("\n",self.Books[x]['Author'])
            #print("\n",self.Books[x]['Price'])
    def savebook(self):
        filename = input("Enter the name of the file:")
        for x in self.Books:
            self.Books[x]['Price'] = str(self.Books[x]['Price'])
            content += str(x +"\n" + self.Books[x]['Author'] + "\n" + self.Books[x]['Price'])
        with open(filename, "w") as file:
            file.write(content)
        print("Book saved successfully.")
    def loadbook(self):
        file_look = input("\nEnter the name of the file you need:")
        try:
            with open(file_look, "r") as file_look:
                for i in file_look:
                    print(i)
        except:
            print ("File wasn't found")
