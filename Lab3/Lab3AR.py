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

for line in lines:
    objectShape = line.rsplit("")
    if objectShape[0] == 'Rectangle':
        Rectangle.length == objectShape[1]
        Rectangle.width == objectShape[2]
    print(line)



file.close()