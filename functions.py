#functions
'''def add(a,b):
    c=a+b
    return c
print (add(5,6))'''
#functions i/o
'''def sum(a,b):
    return a+b;
a=int(input('Enter a : '))
b=int(input('Enter b : '))
print("Total : ",(sum(a,b)))'''
#functions palindrome
'''def palindrome(a):
    a=a.lower()
    if a==a[::-1]:
        print('palindrome')
    else:
        print('not palidrome')
palindrome('malayalam')'''        
#factorial
def fact(a):
    a=int(a)
    b=1
    for i in range(1,a+1):
        b*=i
        print (b)
fact(4)        
