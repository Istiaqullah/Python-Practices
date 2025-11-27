class books:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

class Library:
    def __init__(self):
        self.Books={}

    def addBook(self,book):
        if book.isbn in self.Books:
            print("Book exist")
        else:
            self.Books[book.isbn]=book


    def removeBook(self,isbn):
       if isbn in self.Books:
           self.Books.pop(isbn)
       else:
           print("not found")



    def SearchByTitle(self,title):
        l=[]
        for i in self.Books.values():
            if i.title==title:
                l.append(i)
        return l

    def printAll(self):
        for i in self.Books.values():
            print(f'Name : {i.title}')
            print(f'Author : {i.author} ')
            print('---------------')

b1=books('a','x',75)
b2=books('b','y',76)
b3=books('c','z',77)
l1=Library()
l1.addBook(b1)
l1.addBook(b2)
l1.addBook(b3)

l1.printAll()
print()
print('After removing: ')
l1.removeBook(75)

l1.printAll()



