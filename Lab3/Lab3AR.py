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
completeList = []
for line in lines:
    # goes through and removes commas so lines are like 
    # ['Rectangle', '1', '5\n'] - intsare currently strings and need to be casted
    objectShape = line.rsplit(",")
    if objectShape[0] == 'Rectangle':
        length = int(objectShape[1])
        width = int(objectShape[2])
        completeList.append(Rectangle(length, width))
    elif objectShape[0] == 'Triangle':
        length = int(objectShape[1])
        width = int(objectShape[2])
        completeList.append(Triangle(length, width))
    elif objectShape[0] == 'Circle':
        radius = int(objectShape[1])
        completeList.append(Circle(radius))

for i in completeList:
    print(round(i.getArea(),2))

file.close()