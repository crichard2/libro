#cap 13 challenges

#1

class Cuadrado:
    cuadrados_lista = []
    def __init__(self,lado):
        self.lado = lado
        self.cuadrados_lista.append(lado)
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.lado,self.lado,self.lado,self.lado)

#2

def is_o_no_is(a,b):
    if a is b:
        return True
    else:
        return False

c1 = Cuadrado(2)
c2 = c1
c3 = Cuadrado(3)
print(c1)
print(is_o_no_is(c1,c2))
print(is_o_no_is(c1,c3))
