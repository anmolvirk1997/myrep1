#variables and assignments
#integers
myint = 7
print(myint)
#floats
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
#strings
mystring = 'hello' #we can use ' or " quotes but " is preferred when string in itself contains ' quotations.
print(mystring)
#assignment and output
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
#simultaneous assignment
a, b = 3, 4
print(a,b)

# exercise
mystring = "hello" #remember ""
myfloat = float(10) #or 10.0
myint = int(20) #or 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

#swapping variable
a=5
b=6
temp=a
a=b
b=temp
print(a,b)
#another method
a=a+b               #a=11
b=a-b                #b=11-6=5
a=a-b                   #a=11-5=6
print(a,b)
#another method
a=a^b                 #xor function
b=a^b
a=a^b
print(a,b)
#one line
a,b=b,a
print(a,b)





