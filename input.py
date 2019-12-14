#type casting
'''a=int(input('Enter number one :'))
b=int(input('Enter numer second :'))
print (type(a))
print (type(b))
c=str(a+b)
print("Sum of number is : "+c)'''
#list access
'''a=[1,2,3,'string',[4,5,6]]
a.index(3)
print(a)'''
#flow control
'''a=9
if a>9:
    print('a is greater')
elif a==9:
    print('a is equal')
else :
    print('a is less than')'''
#for loop
'''a=[4,9,6,8]
for i in a:
    print(i)'''
#for loop
'''a=[2,3,5,6,7,3,9,8,4,6,7,12]
for i in range(0,len(a)):
    print (a[i])'''
#for loop addition
'''a=[4,3,6,8,2]
for i in range(0,len(a)):
    a[i]=a[i]+2;
    print(a[i])'''
#for loop sum
'''a=[32,5,7,4,9,15]
print(sum(a))'''
# for loop count
'''a=[5,9,3,8,1,6]
count=0
for i in a:
    count=count+1;
print(count)'''
# for loop sum count
'''a=[6,3,8,9]
sum=0
for i in a :
    sum=sum+i;
    print (sum)'''
# for+ loop number count
'''a=[3,7,9,12,3,5,6,5,4]
b=int(input('number : '))
sumcount=0
for i in a:
    if i==b:
        sumcount=sumcount+1;
print(sumcount)'''
#biggest number
'''a=[4,9,6,71,8,13]
maxvalue=a[0];
for i in a:
    if maxvalue<i:
        maxvalue=i
print (maxvalue)'''
# duplicate
'''a=[3,7,4,5,3,2,9]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    print(b)'''
# divide by 3 and 5
'''a=[]
for i in range(1,100):
    if i%5==0 or i%3==0:
        a.append(i)
print(a)'''
# Input duplicate number
'''a=[5,7,5,2,9,6,3,9]
b=int(input('Enter Number : '))
c=0
for i in a:
   if i==b:
      c+=1
print (c)'''
# Input Max number
'''a=[5,9,2,4,56,1]
max=a[0];
for i in a:
        if max<i:
            max=i
print(max)'''
# Print excluding String
'''a=[6,3,5,8,'ufstrwt',2]
sum=0
for i in a:
     if type(i)==int:
         sum=sum+i
print(sum)'''
# Second Largest Number
'''a=[7,9,4,3,12,11,5]
second_max=0
for i in a :'''
# Diff between sum of square & square of sum
'''a=int(input('enter a number : '))
k=0
sum=0
for i in range(1,a+1):
    j=i**2
    sum=sum+j
    print(sum)
    k=k+i
    l=k**2
    print(l)
print(abs(sum-l))'''
# Extracting alpha
'''a='azya135fd096lui'
b=''
for i in a:
    if i.isalpha():
        b=i
        print(b,end=' ')'''
# Extracting Spl Charectors
'''a='a$@^rtu4435&*'
b=''
for i in a:
    if not i.isalnum():
        b=i
        print(b,end=' ')'''
# Factorial
'''a=int(input('Enter a number : '))
b=1
for i in range(1,a+1):
    b=b*i
    print(b)'''
# Factorial Reverse
'''a=int(input('Enter a number : '))
b=1
for i in range(a,0,-1):
    b=b*i;
    print(b)'''
# Leap Year
'''a=int(input('Enter Year : '))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print(a,' leap year')
        else:
            print('not leap year')
    else:
        print(a,'leap year')
else:
    print(a,' not leap year')'''
# String Formats
'''training=input('Enter course : ')
course=input('Title : ')
print('Hi {} welcome to {} '.format(training,course))'''
# Returning command
'''
start=0
stop=0
while True:
    action=input('Enter Start Command : ')
    if action=='start':
        if start==0:
            print('Car Started ')
            start=1
        elif start==1:
            print('already car started')
    elif action=='stop':
        print('Car Stopped')
    elif action=='exit':
        break
    else:
        print('sorry I dont understand')'''
# Start Stop Flag
'''started= False
while True:
    command=input('Enter the command')
    if command=='start':
        if not started:
            print('start the car')
            started=True
        else:
            print('car already started')
        
    elif command=='stop':
        if not started:
            print('car already stopped')
        else:
            print('stop the car')
            started=False
    elif command=='exit':
        break
    else:
        print('i dont understand')'''
# Slicing
'''a='BITA ACADEMY'
print(a[0:4])
print(a[5:12])
print(a[-len(a):])
print(a[0:12:2])'''
# Slicing Interview
'''st='abcd'
a=int(input('Enter num : '))
print(st[a:]+st[:a])'''
# palindrome
'''st=input('Enter string : ')
reverse=(st[::-1])
print(reverse)
if st==reverse:
    print('palindrome')
else:
    print('not palindrome')'''
#if else practise
age=int(input('Enter age : '))
if 0<age<=10:
    print('children')
elif 10<age<=20:
    print('youth')
elif 20<age<=40:
    print('mid age')
elif 41<age<=60:
    print('senior')
else:
    print('invalid age')
   


        




































