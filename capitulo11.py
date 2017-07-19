#capitulo 11: paradigmas

#state:  valor de una varialbe miesntras se corre el programa
#global state: valor de la variable global

#prrgamacion funcional: se basa en funciones que no usan o cambian global state
#, elimina el side effect (cambiar variables gobales sin intecion)

#ejemplo

a = 0

def increment():
    global a
    a +=1

#una funcion sin side effect seria asi:

def increment(a):
    return a + 1

#object orientes prrgramming: elimina el global state, almacenando la info en objetos
#classes: deine un set de objetos que interactuan entre ellos
#cada objeto es una isntancia de una clase
#convencion: las clases se escriben siempre con la primera letra en mayusucula EstoEsUnaClase
#metodos son como funciones pero se definen dentro de una clase y solo se pueden llamar en el objeto que creo la clase

class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created")

    def rot(self,days,temp):
        self.mold = days * temp

#cualquier metodo rodeado de ""__"" es llamado un metodo magico, para propositos especiales como crear objetos

or1 = Orange(10,"dark orange")
print(or1)
print(or1.weight)

or1.weight = 100

print(or1.weight)

or2 = Orange(4,"light orange")
or3 = Orange(14, "yellow")

print(or1.mold)

or1.rot(10,98)

print(or1.mold)

class Rectangle():
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.area())


