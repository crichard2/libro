#capitulo 13: mas clases

#dos tipos de variables en las clases
#-Class variables:
#ejemplo: recs es una class variable
class Rectangulo():
    recs = []
    def __init__(self,l,a):
        self.largo = l
        self.ancho = l
        self.recs.append((self.largo,self.ancho))
    def print_size(self):
        print("{} by {}".format(self.largo,self.ancho))

r1 = Rectangulo(10,24)
r2 = Rectangulo(20,40)
r3 = Rectangulo(100,200)
print(Rectangulo.recs)

#-Instance variables:
#ejemplo: width y len son instance variables

class Rectangle():
    def __init__(self,w,l):
        self.width = w
        self.len = l
    def print_size(self):
        print("{} by {}".format(self.width,self.len))

#magia

class Lion():
    def __init__(self,nombre):
        self.nombre = nombre
    def __repr__(self):
        return self.name
lion = Lion("pepe")
print(lion)

class AlwaysPositive:
    def __init__(self,numero):
        self.n = numero
    def __add__(self,other):
        return abs(self.n + other.n)
x = AlwaysPositive(-20)
y = AlwaysPositive(10)
print(x+y)

#Is: return True si dos objetos son el mismo y Falso si no

class Person:
    def __init__(self):
        self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)

antoher_bob = Person()

print(bob us another_bob)

x = 10
if x is None:
    print("x is None")
else:
    print("x is not None")
