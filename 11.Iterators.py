#iterator is an iterable object that gives one value at a time when iterated
#in python lists,tuples,strings etc. are iteratorable.
list=[1,2,3,4,4]
x=iter(list)
print(x.__next__())             #next method to get one value at a time
print(next(x))                      #next function to get one value i.e. next value
for i in x:                         #only print remining values as iterator remembers the last value
    print(i)
for i in x:                         #prints no value as iterator has been iterated
    print(i)
for i in list:
    print(i)

#creating an iterator
class topten:
    def __init__(self):
        self.a=1
    def __iter__(self):             #defines the object as iterable for for loop
        return self
    def __next__(self):
        if self.a<=10:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
a=topten()
print(a.__next__())
print(next(a))
for i in a:
    print(i)

#generator as iterator
def fun():
    yield 5                     #function with yield statement is a generator
    yield 6                      #2nd iteration
    yield 7
x=fun()
print(x.__next__())
print(next(x))
for i in x:
    print(i)

def sq():                   #first 10 perfect squares using generator
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
x=sq()
for i in x:
    print(i)
    int