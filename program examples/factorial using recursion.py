def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
x=5
print("Factorial of %d is %d."%(x,fact(x)))
print("Factorial of {} is {}.".format(x,fact(x)))
print("Factorial of {} is".format(x),fact(x),".")