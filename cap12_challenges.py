#capitulo 12 challenges

# 3
class Shape():
    def what_am_i(self):
        print("I am a shape")
        
#1

class Rectangle(Shape):
    def __init__(self,largo,ancho):
        self.largo = largo
        self.ancho = ancho
    def calculate_perimeter(self):
        return 2*self.largo + 2*self.ancho

# 2
class Square(Shape):
    def __init__(self,lado):
        self.lado = lado
    def calculate_perimeter(self):
        return 4*self.lado
    def change_size(self,n):
        return self.lado + n



cuadrado = Square(2)
rectangulo = Rectangle(2,4)
cuadrado.what_am_i()
rectangulo.what_am_i()

#4
class Horse():
    def __init__(self,nombre,jinete):
        self.nombre = nombre
        self.jinete = jinete
class Rider():
    def __init__(self,nombre):
        self.nombre = nombre

tatan = Rider("Tatan")
caballo = Horse("Tatan",tatan)
print(caballo.jinete.nombre)
