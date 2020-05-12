#arithmatic operators
number = 1 + 2 * 3 / 4.0
print(number)

#modulus
remainder = 11 % 3
print(remainder)

#power
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#operator with strings
helloworld = "hello" + " " + "world"  #to give space
print(helloworld)
#repeating string
lotsofhellos = "hello" * 10
print(lotsofhellos)

#operator on lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
#repeat list
print([1,2,3] * 3)

#exercise
x = object()
y = object()

# TODO: change this code
x_list = [x]*10
y_list = [y]*10
big_list = x_list+y_list

print("x_list contains %d objects" % len(x_list)) #len function for length of object
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

#bitwise operators
print(10|11) #bitwise or
print(10&11) #bitwise and
print(10^11) #bitwise xor
print(~10)   #bitwise not
print(10<<2) #bitwise left shift
print(10>>2) #bitwise right shift

#maths module
import math
print(math.sqrt(25))
print(math.pow(2,3))
import math as m #alias
print(m.sqrt(25))
print(m.floor(2.6))
print(m.ceil(2.2))
print(m.comb(5,3))
print(m.fabs(-12))  #absolute value
print(m.factorial(4))
print(m.fmod(21,5))
print(m.frexp(7))
print(m.fsum([12,13,14])) #sum of sequence
print(m.gcd(424,226))
from math import pow,sqrt #import functions from module
print(math.pow(2,8))