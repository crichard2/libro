#desafios capitulo 4
#1
def f(x):
    return x**2
#2
def h(x):
    return print(x)
#3
def g(x,y,z,w=1,v=1):
    return x+y+x+w+v
#4
def primera(x):
    x=int(x)
    return x/2
def segunda(y):
    y=int(y)
    return y*4
x = primera(10)
segunda(x)
#5
def cambio(x):
    try:
        return float(x)
    except ValueError:
        print("invalid input")

print(f(2),h(2),g(1,2,3),cambio("si"))
