#mutiple inheritance
'''class oldcalc():
    a=100
    print('hi')
    def add(a,b):
        c=a+b
        return c
    def sub(a,b):
        c=a-b
        return c
0print(oldcalc.add(10,20))
print(oldcalc.sub(15,25))
class newcalc(oldcalc):
    def mul(c,d):
        e=c*d
        return d
    def div(x,y):
        z=x/y
        return z
print(newcalc.mul(3,5))
print(newcalc.div(6,2))
print(oldcalc.add(7,8))
class moderncalc(newcalc):
    def power(a,b):
        c=a**b
        return c
print(moderncalc.power(3,5))'''
#self
'''class oldcalc:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

obj=oldcalc(10,20)
print(obj.add())
print(obj.sub())'''
#polymorphism
class dog():
    def sound(self):
        print('bark')
class cat():
    def sound(self):
        print('meow')
def mammal(animaltype):
    animaltype.sound()
dogobj=dog()
catobj=cat()
mammal(dogobj)
mammal(catobj)
