class calc():
    a=100
    print('hi')
    def add(a,b):
        c=a+b
        return c
    def sub(a,b):
        c=a-b
        return c
print(calc.add(10,20))
print(calc.sub(15,25))
class incalc(calc):
    def mul(c,d):
        e=c*d
        return d
    def div(x,y):
        z=x/y
        return z
print(incalc.mul(3,5))
print(incalc.div(6,2))
print(calc.add(7,8))
