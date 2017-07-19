#capitulo 7: loops

name = "ted"

for character in name:
    print(character)
    

shows = ["got","narcos","rick y morty"]

for show in shows:
    print(show)
    
coms = ("a. development", "friends", "modern family")

for show in coms:
    print(show)

    
people = {"g. bluth II":"a. development","barney":"hymym","gloria":"modern family"}

for character in people:
    print(character)

i = 0

for show in shows:
    # index variable: variable que guarda el numero que representa el indice en un iterable, en este caso es "i"
    new = shows[i]
    new = new.upper()
    shows[i] = new
    i += 1
print(shows)

#otra forma de escirbir lo mismo

for i,show in enumerate(shows):
    new = shows[i]
    new =  new.lower()
    shows[i] = new

print(shows)

all_shows = []

for show in shows:
    show = show.upper()
    all_shows.append(show)
for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

#rango: una funcion que toma dos parametros, un numero donde la secuencia comienza y el numero donde termina
#la secuencia de numeros que entrega range incluye el primero pero no el segundo

for i in range(1,11):
    print(i)

#while: se ejecuta mientras la expresion sea True

x = 10

while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy new year")

#loops infinitos while True, se puede usar break para cortarlos

for i in range(0,100):
    print(i)
    break

preguntas = ["Como te llamas?","Cual es tu color favorito?","Cual es tu comida favorita?"]
respuestas = ["ah te llamas ","que feo es el ", "a mi no me gusta el "]
n = 0

while True:
    print("Type q to quit")
    a = input(preguntas[n])
    if a == "q":
        break
    print(respuestas[n]+a)
    n = (n+1) % 3 #buen truquillo eh: para iterar siempre dentro de las preguntas
    
#contiue: para saltarse una iteracion

for i in range(1,6):
    if i == 3:
        continue
    print(i)

i = 1

while i <= 5:
    if i == 3:
        i +=1
    print(i)
    i += 1

#nested loops

for i in range(1,3):
    print(i)
    for letter in ["a","b","c"]:
        print(letter)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []
for i in list1:
    for j in list2:
        added.append(i+j)
print(added)

