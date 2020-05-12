x=open('13.file handling read','r')     #to open and read a file
print(x)
print(x.readline())             #reads and print 1st line, bracket specify no of characters
print(x.readline())             #next line
print(x.readlines())            #reads all/remaining lines and print as a list
y = open('13.file handling read', 'r')
print(y.read())                 #read and print entire file
a=open('13.file handling write','w')            #create/open a file to write
a.write('hello')
a.write('anmol')
a.write('\nhello')
b=open('13.file handling write','a')        #open a file to append date
b.write(' Anmol')
c=open('DSC_0033.jpg','rb')                 #rb to read binary data in files
for i in c:
    print(i)
d=open('newpic.jpg','wb')                        #Wb to write binary
c=open('DSC_0033.jpg','rb')                      #open the file again to read and iterate from start
for i in c:
    d.write(i)