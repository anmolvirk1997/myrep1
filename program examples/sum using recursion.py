def sum_n(n):
    if n == 1 or n == 0 :
        return n
    else:
        return n+sum_n(n-1)
print (sum_n(100))