class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False
    def check_out(self):
        self.__is_checked_out = True
    def return_book(self):
        self.__is_checked_out = False
    def check_status(self):
        return self.__is_checked_out
class Library:
    __books = []
    
    @classmethod
    def add_book(cls, my_book):
        cls.__books.append(my_book)
    
    @classmethod
    def check_out_book(cls, title):
        i = 0
        while i < len(cls.__books):
            if cls.__books[i].title == title:
                cls.__books[i].check_out()
                break
            #This function doesn't do anything if the book title passed doesn't exist in the list.
            i += 1
        
    @classmethod
    def return_book(cls, title):
        i = 0
        while i < len(cls.__books):
            if cls.__books[i].title == title:
                cls.__books[i].return_book()
                break
            #This function doesn't do anything if the book title passed doesn't exist in the list. 
            i += 1

    @classmethod
    def list_available_books(cls):
        for i in cls.__books:
            if i.check_status():
                pass
            else:
                print(f"{i.title} by {i.author}")

            
    
