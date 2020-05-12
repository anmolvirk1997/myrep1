i=1
while  i<=10:
    print('anmol')
    i+=1

for i in range(1,11):       #loop for is used for looping over a given sequence e.g. range, list etc.
    print(2*i)

for i in range(1,101):
    if i%2!=0:
        continue            #continue statement is used for skipping the iteration when if condition is true.
    print(i)

for i in range(1,11):
    if i>=5:
        break               #break statement is used to terminate the loop when if condition is true.
    print(2*i)

for i in range(1,11):
    if i==6:
        pass               #pass is an empty statement it does nothing when if is true.
    print(2*i)

for i in range(1,11):
    if i==6:
        pass                #pass with else can be used as continue.
    else:
        print(2*i)

x=None
for i in [1,2,3,4,5,6,7,8,9]:   #program to find even numbers
    if i%2==0:
        x=i
        print(x)
        continue
if x==None:
    print('not found')

x=int(input('Enter a number:'))
for i in range(2,x):
    if x%i==0:
        print('Not Prime')
        break
else:
    print('Prime')
