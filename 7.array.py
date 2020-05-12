#list as array-list can contain elements of multiple types unlike array
list=[[[1,2,3],[4,5,6],[7,8,9]],[['anmol','gourav','pardeep'],['virk','sain','donkle']]]
print(list[1][0][0],list[1][1][0])

import array as arr
val=arr.array('i',[1,2,4,5,8,89,8])
print(val[1])

from array import *
val = array('i',[1,2,3,4,5,6,7])
for i in val:
    print(i)

arr=array('i',[])
x=int(input('Enter the length'))
for i in range(x):
    n=int(input('Enter the value'))
    arr.append(n)
print(arr)

val=int(input('Enter the value to search'))
k=0
for i in arr:
    if i==val:
        print(k)
        break
    k+=1

print(arr.index(val))

from numpy import *
arr=array([1,2,4,5])
print(arr)
arr=linspace(0, 15,10) #like range start to stop(included) and number of parts default 50
print(arr)
arr=arange(1,12,2)
print(arr)
arr=logspace(1,10,3)
print(arr)
arr=zeros(5)
print(arr)
arr=ones(7)
print(arr)

from numpy import *
arr1=array([1,2,3,4,5])
arr2=array([6,7,8,9,0])
print(arr1+arr2)        #adds corresponding elemnets or arrays
arr=arr1+5              #adds 5 to all elements of array
print(arr)
print(concatenate([arr1,arr2]))
arr=arr1.view()                     #copies the array with changes made
print(arr)
arr1[1]=19
print(arr)
arr=arr1.copy()                     #deep copy 
arr1[1]=10
print(arr)

from numpy import *
arr=array([[1,2,3,4,5,6],[6,7,8,9,0,1]])
print(arr.flatten())                #converts to one dimensional
print(arr.reshape(2,2,3))            #convert array into 2*2*3 dimensions

a=[[1,2,3],             #list as matrix and function for multiplication of matrix
   [4,5,6]]
b=[[10,11,12,13],
   [12,13,14,15],
   [14,15,16,17]]
def mml(x,y):
    if len(x[0])==len(y):           #check matrix conpatibility
        a=len(x)
        b=len(x[0])
        c=len(y[0])
        z=[[],[]]
        sum=0
        for i in range(a):
            for j in range(c):
                for k in range(b):
                    sum=sum+x[i][k]*y[k][j]
                z[i].insert(j,sum)
                sum=0
        print(z)
    else:
        print('Matrix are not compatible')
mml(a,b)

from numpy import *
a=matrix('1 2 3; 4 5 6')            #matrix function
b=matrix('10 11; 12 13; 14 15')

print(a*b)
