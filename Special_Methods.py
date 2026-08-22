class Book:
    # __init__() is a constructor.
    # It is automatically called when an object is created.
    def __init__ (self, title, author):
        self.title = title 
        self.author = author
    # __str__() defines the string representation of an object.
    # It is automatically called when we use print(object).
    def __str__(self):
        return f"'{self.title}' by {self.author}"    
b = Book("1984", "George Orwell")
print(b)

class Playlist:
    def __init__(self, song):
        self.songs = song

# __len__() and __add__() are special methods
# __len__() returns the length of the object
# __add__() defines how two objects are added

    def __len__(self):
        return len(self.songs)
    def __add__(self, other):
        return Playlist(self.songs + other.songs)    
p1 = Playlist(["Song1" , "Song2"])
p2 = Playlist(["Song3"])
print(len(p1))
print(len(p1 + p2))

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x} , {self.y})"
    def __add__(self, other):

    # isinstance() checks whether other is a Point object    
        if not isinstance(other, point): 
            return NotImplemented
        return point(self.x + other.x, self.y + other.y)
p1 = point(6, 4)
p2 = point(2, 6)    
print(p1 + p2)
