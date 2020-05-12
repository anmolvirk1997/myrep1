#taking input
x=input()
y=input()
print(x+y)

x=input('Enter first number:')  #with input prompt
y=input("Enter second number:")
print(x+y)

x=int(input("Enter 1st number:"))  #input as integers, as by default input is as string
y=int(input("Enter 2nd number:"))
print(x+y)

x=input("Enter an input")[0] #takes only 1st character
print(x)

x=eval(input('Enter an expression:')) #evaluates the input
print(x)