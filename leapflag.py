'''a=int(input('Enter year : '))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print(a,' leap year')
        else:
            print('not leap year')
    else:
         print('leap year')
else:
    print(a,' not leap year')'''
# slicing of strings
'''st='abcd'
a=int(input('Enter num : '))
print(st[a:]+st[:a])'''
# palindrome
'''st=input('Enter string : ')
reverse=st[::-1]
#st[::]==st[-1::-1]
print(reverse)
if st==reverse:
    print ('palindrome')
else:
    print ('not palindrome')'''
# string functions
'''a='arunacademy'
print (a.upper())
print (a.lower())
print (a.capitalize())
print (a.casefold())
print (a.title())
print (a.center(30))'''
# Extracting Special Integer String
'''a='ab135-@$#!^kdjkdsvnk7663'
for i in a:
    if i.isalpha():
        print(i,end=' ')
print()
for i in a:
    if i.isdigit():
        print(i,end=' ')
print()
for i in a:
    if not i.isalnum():
        print(i,end='')'''
#String Split
'''a='bita academy'
a=a.split('a')
print(a)'''
#String join
'''a=['b''i''t''a']
a=''.join(a)
print(a)'''
#number split
'''a=input('Enter list : ')
a=a.split()
b=0'''
'''for i in range(len(a)):
    a[i]=int(a[i])
print(a)'''
'''for i in a:
    a[b]=int(i)
    b+=i
print(a) '''   
# tuple
'''a=(10,20,33,33)
b=tuple(a)
print(b)
print(b.count(33))
print(b.index(20))'''
# set methods
'''set1={1,2,3,4,5,6,7}
set2={1,2,4,5,6,9}
print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set2-set1)'''
# dictonary methods
dict={'a':'apple','b':'ball','c':['cat','camel']}
print(dict['a'])
print(dict['b'])
print(dict['c'])
dict1={'count':{'india':['chennai','madurai']}}
print(dict1)
print(dict1['count']['india'][1])

