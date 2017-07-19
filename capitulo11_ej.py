#challeges:

#1

class Apple:
    def __init__(self,color,weight,acidity,days):
        self.color = color
        self.weight = weight
        delf.acidity = acidity
        self.days = days

#2

class Circle:
    def __init__(self,r):
        self.radio = r

    def area(self):
        import math
        return math.pi*self.radio**2

import math
circulo = Circle(math.sqrt((1/math.pi)))
print(circulo.area())

#3

class Triangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def area(self):
        return self.a*self.b*0.5

tri = Triangle(3,4)
print(tri.area())
#4

class Hexagon:
    def __init__(self,a):
        self.a = a

    def calculate_perimeter(self):
        return 6*self.a

hexa = Hexagon(2)
print(hexa.calculate_perimeter())

    
