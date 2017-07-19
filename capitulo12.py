#capitulo 12

#encapsulation:
#primero

class Rectangle():
    def __init__(self,w,l):
        self.width = w
        self.len = l
    def area(self):
        return self.width*self.len
        

#segundo: privacidad
# usar '_' antes de la variable para declararla privada (convencion)
class Data:
    def __init__(self):
        self.nums = [1,2,3,4,5]

    def change_data(self,index,n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0,100)
print(data_two.nums)

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsaf"

    def public_methos(self):
        pass

    def _unsafe_method(self):
        pass

#abstraction

#polymothphism

#inheritance

class Shapes():
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}""".format(self.width,self.len))

my_shape = Shapes(20,25)
my_shape.print_size()

#se puede llamar a otra clase desde otra
class Square(Shapes):
    def area(self):
        return self.width*self.width
    def print_size(self):
        #se pueden reescribir los metodos
        print("I am {} by {}".format(self.width,self.len))

a_square = Square(20,20)
a_square.print_size()
print(a_square.area())


#composicion

class Dog():
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self,name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley","Bulldog",mick)
print(stan.owner.name)







              
