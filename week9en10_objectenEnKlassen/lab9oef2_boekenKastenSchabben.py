class Boek():
    def __init__(self, title, author, price, thickness):
        self.title = title
        self.author = author
        self.price = price
        self.thickness = thickness
    
class Kast():
    def __init__(self, *shelves):
        self.shelves = shelves
        self.space = 0
        for shelve in self.shelves:
            self.space += shelve.space
        self.spaceTaken = 0
        self.books = []

    def voeg_boek_toe(self, *newBooks):
        self.spaceTaken = 0
        for newBook in newBooks:
            bookAdded = False
            for schab in self.shelves:
                if (((schab.spaceTaken + newBook.thickness) < schab.space) or (schab.full == False)):
                    if (bookAdded == False):
                        schab.add_book(newBook)
                        self.books.append(newBook)
                        bookAdded = True
        for schab in self.shelves:
            self.spaceTaken += schab.spaceTaken
            
                
    
    def totale_prijs(self):
        total = 0
        for book in self.books:
            total += book.price
        return total
    
    def bevat_boek(self, title):
        titles = []
        for book in self.books:
            titles.append(book.title)
        if title in titles:
            return True
        else:
            return False

class Schab():
    def __init__(self, space):
        self.space = space
        self.spaceTaken = 0
        self.full = False
        self.books = []

    def add_book(self, newBook):
        if (self.spaceTaken < self.space):
            if ((self.spaceTaken + newBook.thickness) <= self.space):
                self.books.append(newBook)
                self.spaceTaken += newBook.thickness
            else:
                print(f"not enough space left to add book: {newBook.title} to shelve ({(newBook.thickness + self.spaceTaken) - self.space}cm too thick)")
        else:
            print(f"cannot add book {newBook.title}: schab is full")
            self.full = True
        
        
    
testboek1 = Boek("test1", "ikke", 5, 20)
testboek2 = Boek("test2", "iemand anders", 2, 10)
testboek3 = Boek("dikkerik", "anoniem", 50, 40)
testboek4 = Boek("dun ding", "anoniem", 50, 5)
testboek5 = Boek("dingeske", "mark", 10, 25)

schab1 = Schab(30)
schab2 = Schab(5)
schab3 = Schab(10)


kast1 = Kast(schab1, schab2, schab3)

kast1.voeg_boek_toe(testboek1, testboek2, testboek3)

print(kast1.totale_prijs())

print(kast1.bevat_boek("test1"))
print(kast1.bevat_boek("nee hoor"))

kast1.voeg_boek_toe(testboek4, testboek5)
kast1.voeg_boek_toe(testboek3, testboek5)

print(f"{kast1.spaceTaken}/{kast1.space}")

print(f"{schab1.spaceTaken}/{schab1.space}")

print(f"{schab2.spaceTaken}/{schab2.space}")

print(f"{schab3.spaceTaken}/{schab3.space}")
