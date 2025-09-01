# def Drive(car):
#     car.drive()
# class Nissan:
#     def drive(self):
#         print("we are in nissan car")

# class BMW:
#     def drive(self):
#         print("we are in BMW car")   

# n = Nissan()
# Drive(n)
'''
def petLover(pet):
    pet.talk()
    pet.walk()

class Duck:
    def talk(self):
        print('duck is talking')
    def walk(self):
        print('Duck is walking')
class Dog:
    def talk(self):
        print('Dog is talking')
    def walk(self):
        print('dog is walking')
        
d= Duck()
petLover(d)
do= Dog()
petLover(do)'''
'''
class Algeb:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c):
        return a+b+c
    
a = Algeb()
print(a.sum(5,6,7))
print(a.sum(5,9))
'''
'''
class Algeb:
    def sum(self,a,b,c=None):
        s= a+b
        if (c==None):
            return s
        else:
            return s+c
    
a = Algeb()
print(a.sum(5,6,7))
print(a.sum(5,9))
'''
'''
class iphone16:
    def home(self):
        print('home button e is pressed')
    
class iphone17(iphone16):
    def home(self):
        print("home button is running")
        super().home()

i6 = iphone16()
i6.home()
i7 = iphone17()
i7.home()
'''
'''
# todo
class Rational:
    def __init__(self, p=1, q=1):
        self.p = p
        self.q = q  
    def __add__(self, other):
        s = Rational()
        s.p = self.p * other.q + self.q * other.p #Numerator
        s.p = self.p * other.q #denominator
        return s   
    def __str__(self):
        return str(self.p)+'/'+str(self.q)

r1= Rational(2,3)
print(r1.p, r1.q)
r2= Rational(3,4)
print(r1.p, r1.q)
sum = r1+r2
print(sum.p,sum.q)
'''
'''
from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def show(self):
        pass
    
    def display(self):
        print('Displayed parent')
    
class Child(Parent):
    def show(self):
        print('Display child method')

c= Child()
c.show()
c.display()
'''
'''
class A:
    def show(self):
        print('Class A is here')

class B(A):
    pass
b=B()
b.show()
print(B.mro())
'''    
'''
class A:
    def show(self):
        print('Class A is here')
class B(A):
    pass
class C(B):
    pass
c=C()
c.show()
print(C.mro())     
'''
'''
class A:
    pass
class B:
    pass
class C(A, B):
    def show(self):
        print('Class c is here')
c=C()
c.show()
print(C.mro()) 
'''
'''
class A:
    pass
class B:
    def show(self):
        print('Class b is here')
    
class C(A, B):
    pass
c=C()
c.show()
print(C.mro()) 
'''
'''
_____ represents an entity in the real world with its identity and behaviour. 

    Object 
    Operator 
    Class 
    Method 

Ans: Object


hasattr(obj, name) is used to? 

    Access the attribute of the object 
    Check if the attribute exists or not 
    Delete the attribute 
    Set an attribute 
    
Ans:  Check if the attribute exists or not 


What is the difference between class and an object 

    A blueprint is an object to make a class 
    An object is a blueprint to make a class 
    Blueprint class is an object 
    A class is a blueprint of an object 

Ans: A class is a blueprint of an object 


Theses have identity , state  and behaviour 
    Object 
    Method 
    Void 
    Class 
    
Ans: Object


Which of the following is false about protected class members ? 

    They can be accessed by outside of the class. 
    They can be access by subclass 
    They can be accessed within a class 
    They begin with one underscore 

Ans: They can be accessed by outside of the class.





'''