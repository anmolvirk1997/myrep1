#List ans list index
mylist = []             #defines list
mylist.append(1)        #adds element at the end of the list
mylist.append(2)        #index is zero based
mylist.append(3)
print(mylist[0]) # prints 1 at index 0 
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3


# prints out 1,2,3
for x in mylist:
    print(x)

mylist = [1,2,3] #another way, can also use () brackets
print(mylist[1])      #list index should be in range here cant be >2




numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_name=names[1]
# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

#indexing of list
a=[1,2,5,6]
b=['anmol','sagar','pardeep','gaurav','varun']
print(a[1]) #prints the list element on specified index
print(b[2:4])   #slice of list between the indices specified
print(b[:3])
print(b[1:])
print(b[1::2]) #every 2nd element

#changing elements
a=[1,2,5,6]
b=['anmol','sagar','pardeep','gaurav','varun']
a[1]='virk' #replaces item at index 1
print(a)
for x in a:  #looping in list
    print(a)
if "anmol" and 'virk' in b:  #checking items in list
    print('yes')
else:
    print('no')

mylist=[1,2,3]
mylist1=['anmol','pardeep','gourav']
mylist.extend((12,34,56))       #adds another iterable(list,tuple,sets) elements to the end of list
print(mylist)
mylist.extend(mylist1)
print(mylist)
mylist.insert(1,0)                  #insert element before specified index
print(mylist)
mylist.pop(3)                     #removes element at specified index otherwise the last element
print(mylist)
del mylist[0]
print(mylist)                   #deletes the element at index specified otherwise the whole list is deleted
mylist1.clear()
print(mylist1)

mylist=[3,4,2,1]                      #removes all items doesn't delete the list
mylist.sort()                          #sorts the elements doesn't work for list containing int and str both
print(mylist)
mylist.reverse()                        #reverse the elements
print(mylist)

mylist=['anmol','anmol',1,1,3]
print(mylist.index('anmol'))            #returns the index of the item
print(mylist.count(1))                     #count the occurence of item in list
a=mylist.copy()                 #copies the list
print(a)
a=list(mylist)              #copies the list
print(a)

a=list((1,2,4))              #construct a new list or empty list
print(a)
print(len(a))               #no. of items




