#parametros opcionales
def f(x=2):
    return x**x
print(f())
print(f(4))

#definir primero los requeridos y despues los opcionales
def g(x,y=2):
    return x+y
print(g(2))
print(g(2,1))

#manejo de excepciones
#no definir variables dentro de try que seran usadas dentro de except
try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("invalid input")
