import math #include pi

#define default class so area can be calculated differently for each shape
class Shape:
    def __init__(self):
        pass
    def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def getArea(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def getArea(self):
        return ((self.length * self.width) / 2)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def getArea(self):
        return ((self.radius ** 2) * math.pi)


#access file in the correct directory and iterate though each line
file = open("shapes.txt", 'r')
lines = file.readlines()
file.close()

for line in lines:
    print(line)