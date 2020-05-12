def greet():                #definition of function
    print('Hello')          #prints when called
greet()

def greet():
    return 'Hello'          #returns a value which can be assigned or printed when called
print(greet())

def greet():
    print('Hello')
print(greet())
a=greet()
print(a)            #assigns none value

def greet(a,b):         #function with defined arguments
    print('Hello,',a,'and',b)
greet('anmol','pardeep')

a=5
print('id of a',id(a))
def val(x):
    print('id of x',id(x))      #address of a and x is same
    x=10                        #value changes in function
    print('id of x',id(x))      #adress of x is changed
    print('a ',x)
val(a)
print('a ',a)                   #value of a outside function is unchanged
print('id of a',id(a))          #adress of a

a=[1,2]
def val(x):
    print(id(x))
    x[0]=0
    print(id(x))            #adress of variable is not changed as variable itself is same
    print(x)
    del x                   #does not delete the list a
val(a)
print(a)

def a(x,*y):                #will assign first value to x and rest of values to tuple y
    print(x,y[0],y[1])       #index shouldn't be out of range of arguments
a(1,1,2,3)

def a(x,*y):
    for i in y:
        print(x,i)      #prints every index value
a(1,1,2,3)


def a(**x):                 #takes values as dict mapping
    print(x['fname'])
a(fname='anmol',lname='virk')

def a(**x):                 #takes values as dict mapping
    for i,j in x.items():
        print(i,j)
a(fname='anmol',lname='virk')

#scope of variable
a,b,c=1,2,3
def fun():
    a=4         #local variable in function doesn't affect global a
    global d     #defines a global variable
    d=5
    x=globals()['b']       #access the global variable outside of function
    globals()['c']=4        #changes value of global variable
    print('a',a)
    print('d',d)
    print('x',x)
fun()
print('a',a)
print('b',b)
print('c',c)
print('d',d)

list=['anmol','pardeep','sandeep']          #list as argument
def fun(a):                                 #function to count a and e
    x,y=0,0
    for i in a:
        x=x+i.count('a')
        y=y+i.count('e')
    return x,y
a,e=fun(list)
print('No. of a is {} and e is {}'.format(a,e))

#function to create fibonacci series
n=int(input("Enter the no. of terms: "))
a0,a1=0,1
while n<=0:
    n=int(input('Enter a number greater than 0: '))
if n==1:
    print(a0)
else:
    print(a0,a1,end=' ')
    for i in range(2,n):
        c=a0+a1
        a0,a1=a1,c
        print(c, end=' ')

#function for factorial
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=int(input('Enter a number: '))
print(fact(x))

#factorial using recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
x=int(input('Enter a no.: '))
print(fact(x))

#anonymous function lambda
x=lambda a,b: a**b          #any no. of arguments but only one expression
print(x(2,3))

#filter,map and reduce
a=[1,2,3,4,5,6,7,8,9,0]
evens=list(filter(lambda n : n%2==0, a))    #filter the elements for which argument function(lambda or predefined function) returns true
print(evens)
doubles=list(map(lambda n:2*n,evens))           #applies the function on elements and returns
print(doubles)
from functools import reduce
sum=reduce(lambda a,b:a+b,doubles)
print(sum)

#decorators
def div(a,b):
    return a/b
def smart_div(func):    #decorator function to modify another function
    def inner(a,b):
        if a<b:
            return func(b,a)
        else:
            return func(a,b)
    return inner
div=smart_div(div)
print(div(2,3))

# function for searching a value in list, linear search
list=[1,2,7,'c',9,0,10,17,56,2]
def search(list,n):
    x,y=[],None
    for i in range(len(list)):
        if list[i]==n:
            x.append(i+1)
            y=True
    if y:
        print('Value {} found at'.format(n),*x, sep=',')
    else:
        print('Value {} is not found in the list'.format(n))
search(list,2)

# Binary search
pos=-1
def search(list,n):
    list.sort()
    global pos
    l=0
    u=len(list)-1
    while l<u:
        mid=(l+u)//2
        if list[mid]==n:
            pos=mid
            return True
        else:
            if list[mid]<n:
                l=mid
            else:
                u=mid
list=[1,2,3,7,4,5,9,4,3]
n=3
if search(list,n):
    print('Found at {}th in ascending order'.format(pos+1))
else:
    print('Not found')

# Function to sort a list
def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]


list=[9,3,2,1,6,5,0,8]
sort(list)
print(list)

# Function to sort a list with minimum position
def sort(list):
    for i in range(len(list)-1):
        minpos=i
        for j in range(i+1,len(list)):
            if list[minpos]>list[j]:
                minpos=j
        list[i],list[minpos]=list[minpos],list[i]


list=[9,3,2,1,6,5,0,8]
sort(list)
print(list)