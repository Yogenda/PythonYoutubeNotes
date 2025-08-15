'''
def display(name):
    print('Hello',name)
    
# display('Abhishek')
d = display
d('Humera')
d('Hemant')
'''
'''
def outer():
    print('this is outer function')
    def inner():
        print('this is inner function')
    inner()
       
outer()
'''
'''
def display():
    print('Hello')
def fun(d):
    d()
    
fun(display)
'''
'''
#adding the behaviour to function
def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def fun(f,x,y):
    f(x,y)

fun(add,10,60)
fun(sub,10,60)
'''
'''
def outer():
    def display():
        print('hello world')
    return display

a = outer()
a()
'''
'''
def closure():
    msg ="Hello" #local for closure fun
    
    def display():
        print('*'*10)
        print(msg) #msg is non local
        print('*'*10)
    return display

d=closure()
d()
'''
'''
def closure(msg):   
    def display():
        print('*'*10)
        print(msg) #msg is non local
        print('*'*10)
    return display

d=closure("Hi all")
d()
'''
'''
class Student:
    def __init__(self):
        self.std={
            'Humera': 'data analysis',
            'Abhishek': 'Web dev',
            'Hemant': 'java',
            'Madhu': 'html'
        }
    def __call__(self,Student):
        return self.std[Student]
    
s = Student()
a=s('Hemant')
print(a)
'''
'''
def student():
    student={
            'Humera': 'data analysis',
            'Abhishek': 'Web dev',
            'Hemant': 'java',
            'Madhu': 'html'
        }
    def stdfun(stud):
        return student[stud]
    return stdfun
    
s = student()
a=s('Hemant')
print(a)
'''