#try and except
a=5
b=int(input("Enter the number:"))
try:                                    #this block will execute if no error is encountered
    print(a/b)
except Exception:                       #this block is executed if error is encountered, except followed by type of error
    print("error")
else:
    print('else')                       #this block will execute if except block is not executed
finally:
    print('final statement')            #this block is executed regardless of any error

#raise an error
a=int(input('Enter a: '))
b=int(input('Enter b:'))
if b==0:
    raise Exception("Zero Error")           #or just raise Exception
else:
    print(a/b)


try:                                   #this block will execute if no error is encountered
    a=5
    b=int(input("Enter the number:"))
    print(a/b)
except ValueError as v:
    print('Oops',v)
except ZeroDivisionError as z:
    print('Oops',z)
    input()

#multithreading
from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(10):                 #method name should be run
            print('Hello')
            sleep(1)
class hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(1)
a=hello()
b=hi()
a.start()                       #start calls run
sleep(0.2)
b.start()
a.join()
b.join()
print('bye')