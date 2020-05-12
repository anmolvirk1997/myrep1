#class is a type or design for and object
class identity:
    def __init__(self,fname,sname,age):             #init called automatically, it identifies the arguments
        self.fname=fname                             #assign the values to instance variable<<instance/object namespce
        self.sname=sname
        self.age=age
        print("Hello",end='')
        self.ht=self.height()                           #call inner class

    def person(self):                           #person is called as an instance method
        print('Mr. {} {} is {} years old.'.format(self.fname,self.sname,self.age))
    weight=60                                   #class variable<<class namespace

    @classmethod
    def getweight(cls):                         #class method for class variables, accepts cls argument
        print(cls.weight)

    @staticmethod                               #static method
    def static():
        print('Hello')

    class height:                               #def inner class
        def __init__(self):
                self.height=1.8

person1=identity('Anmol','Virk',22)             #object person1<<class identity
person2=identity('Pardeep','Donkle',23)

person1.person()                            #Here person1 is passed as self argument to object method person
print(person1.weight)
person1.getweight()
person1.static()

print(type('Anmol'),type(12),type(identity),type(person1))
person1.fname='Ammy'                               #to change the attributes of instance varible
identity.weight=70                                #changes the class variable
person1.person()
print(person1.weight)
identity.getweight()
identity.static()

print(person1.ht.height)                            #calls innerclass

#inheritance
class a:                                #parent class
    def feature1(self):
        print('feature1')
class d:
    def feature4(self):
        print('feature4')
class b(a):                             #child class of a
    def feature2(self):
        print('feature2')
class c(b):                             #child class of b
    def feature3(self):
        print('feature3')
class e(a,d):                           #inherit from a and d seperately
    pass
a=a()
b=b()
c=c()
d=d()
e=e()
a.feature1()
b.feature1()
b.feature2()
c.feature1()
c.feature2()
c.feature3()
d.feature4()
e.feature1()
e.feature4()

#constructor in class
class a1:
    def __init__(self):
       print('Init a1')
    def feature(self):
        print('feature b1')
class a2(a1):                           #inherit init from a1
    pass
class a3(a1):
    def __init__(self):                 #does not inherit init
        print('Init a3')
class a4(a1):
    def __init__(self):
        super().__init__()              #inherit a1 init
        print("Init a4")
class b1:
    def __init__(self):
        print('Init b1')
    def feature(self):
        print('feature b1')
class c1(a1,b1):                       #method resolution order prefer left argument fot inheritance
    pass

a1=a1()
a2=a2()
a3=a3()
a4=a4()
b1=b1()
c1=c1()
c1.feature()

#duck typing
class typea:
    def exe(self):
        print("type a")
class code:
    def run(self,ide):
        ide.exe()                        #method from class/type of variable ide
class typeb:
    def exe(self):
        print('type b')

ide=typea()
code1=code()
code1.run(ide)                      #run is taking arguments as no init is defined in class
ide=typeb()                           #we can change class/type of varaible ide as long as it has same method exe as mentioned in class code
                                    #...method run
code1.run(ide)

#operator overloading-> defining operators for an object in a class
class student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3=self.m3+other.m3
        return student(m1,m2,m3)
    def __gt__(self, value):
        if self.m1>self.m2:
            return True
        else:
            return False
s1=student(89,78,56)
s2=student(80,79,89)
print((s1+s2).m1,(s1+s2).m2,(s1+s2).m3)    # ->student.__add__(self,other)
print(s1>s2)                               # ->studen.__gt__(self,other)


#method overloading and method overriding
class cls:
    def mt(self):
        print('Test cls')
    def mt1(self):
        print('test cls')
class cls2(cls):
    def mt(self):
        print('test cls2')
    def ov(self,a=None,b=None,c=None):             #default values of arguments
        if a!=None and b!=None and c!=None:         #condition for values
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        print(s)
a=cls2()
a.mt1()                         #mt1 method is inherited from parent class cls
a.mt()                          #mt method of cls2 overrides inherited mehtod mt of cls
a.ov()                          #method overloading
a.ov(1)
a.ov(1,2)
a.ov(1,2,3)

