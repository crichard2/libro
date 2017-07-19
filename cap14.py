#cap 14

class Cartas:
    pintas = ["Pic","corazones","diamantes","trebol"]
    valores = [None,None,"2","3","4","5","6","7","8","9","10","Jaco","Cuina","Rey","As"]
    def __init__(self,v,s):
        """suits + calues area ints"""
        self.valor = v
        self.pinta = s
    def __lt__(self,c2):
        if self.valor < c2.valor:
            return True
        if self.valor == c2.valor:
            if self.pinta < c2.pinta:
                return True
            else:
                return False
        return False
    def __gt__(self,c2):
        if self.valor > c2.valor:
            return True
        if self.valor == c2.valor:
            if self.pinta > c2.pinta:
                return True
            else:
                return False
    def __repr__(self):
        v = self.valores[self.valor] + " de " + self.pintas[self.pinta]
        return v

from random import shuffle

class Maso:
    def __init__(self):
        self.cartas = []
        for i in range(2,15):
            for j in range(4):
                self.cartas.append(Cartas(i,j))
        shuffle(self.cartas)

    def rm_card(self):
        if len(self.cartas) == 0:
            return
        return self.cartas.pop()

class Jugador:
    def __init__(self,nombre):
        self.wins = 0
        self.cartas = None
        self.nombre = nombre

class Juego:
    def __init__(self):
        name1 = input("nombre jugador1")
        name2 = input("nombre jugador2")
        self.maso = Maso()
        self.p1 = Jugador(name1)
        self.p2 = Jugador(name2)
    def wins(self,winner):
        w = "{} gana la ronda"
        w = w.format(winner)
        print(w)
    def draw(self,p1n,p1c,p2n,p2c):
        d = "{} saca un {} {} saca un {}"
        d =  d.format(p1n,p1c,p2n,p2c)
        print(d)
    def jugar_juego(self):
        cartas = self.maso.cartas
        print("Que comienze la guerra!")
        while len(cartas) >= 2:
            m = "q to quit.any key to play: "
            respuesta = input(m)
            if respuesta == "q":
                break
            p1c = self.maso.rm_card()
            p2c = self.maso.rm_card()
            p1n = self.p1.nombre
            p2n = self.p2.nombre
            self.draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.nombre)
            else:
                self.p2.wins += 1
                self.wins(self.p2.nombre)
        win = self.winner(self.p1,self.p2)
        print("termino la guerra. {} gana".format(win))
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.nombre
        if p1.wins < p2.wins:
            return p2.nombre
        return "Empate"

juego = Juego()
juego.jugar_juego()
