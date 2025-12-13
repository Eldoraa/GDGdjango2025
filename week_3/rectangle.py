"""4. Rectangle Class 
● Create a class Rectangle with width and height. 
● Print the area (without adding a separate method)."""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(4, 10)
print(r.area())