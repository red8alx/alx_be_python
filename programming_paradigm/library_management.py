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
    def __init__(self):
        self._books = []
    def add_book(self, my_book):
        self._books.append(my_book)
    
    def check_out_book(self, title):
        i = 0
        while i < len(self._books):
            if self._books[i].title == title:
                self._books[i].check_out()
                break
            #This function doesn't do anything if the book title passed doesn't exist in the list.
            i += 1
        
    def return_book(self, title):
        i = 0
        while i < len(self._books):
            if self._books[i].title == title:
                self._books[i].return_book()
                break
            #This function doesn't do anything if the book title passed doesn't exist in the list. 
            i += 1

    def list_available_books(self):
        for i in self._books:
            if i.check_status():
                pass
            else:
                print(f"{i.title} by {i.author}")

            
    
