#we are passing our own function
'''
def decorator(fun):
    def wrapper():
        print('*'*10)
        fun()
        print('*'*10)
    return wrapper
def display():
    print("hello")
    
d=decorator(display)
d()
'''
'''
def decorator(fun):
    def wrapper(msg):
        print('*'*10)
        fun(msg)
        print('*'*10)
    return wrapper
def display(msg):
    print(msg)
    
d=decorator(display)
d("hello")
'''
'''
def decorator(fun):
    def wrapper(msg):
        print('*'*10)
        fun(msg)
        print('*'*10)
    return wrapper
def display(msg):
    print(msg)
    
display=decorator(display)
display("hello")
'''
'''
def decorator(fun):
    def wrapper(msg):
        print('*'*10)
        fun(msg)
        print('*'*10)
    return wrapper
@decorator
def display(msg):
    print(msg)
    
# display=decorator(display)
display("hello")
'''
'''
def m2k(mile):
    k= 1.6*mile
    return k
print(m2k(10))

k = lambda mile:1.6*mile
print(k(10))
'''
'''
def add(a,b):
    c=a+b
    return c
f=lambda a,b: a+b
print(f(10,30))
f=lambda a, b:a if a>b else b
print(f(10,50))
'''
'''
a=int(input('enter the number'))
b=int(input("second number"))
print(a/b)
'''
'''
# d={1:'a',2:'b',3:'c'}
# key = 4
# print(d[key])

l=[1,2,3,4,5,6]
print(l[8])
'''
'''
l=[10,20,30,40,50,60]
try:
    txt = int(input("Enter any nubmer"))
    print(l[txt])
except ValueError:
    print("Enter only nubmer")
except IndexError :
    print("index not present")    
print("i am here...")
'''
'''
l=[10,20,30,40,50,60]
try:
    txt = int(input("Enter any nubmer"))
    print(l[txt])
except (IndexError ,ValueError) as msg:
    print(msg)    
print("i am here...")
'''

'''
Question 1: When a program is in executing  and if the code in the program is
required  to divide a number by zero, then the  program crashes. 
What type of error is it?. 

    a logic error 
    a run-time  (C)
    a user error 
    a syntax error 


Question 2: A syntax error in your code means. 

    you have not used enough characters 
    there was no defined index 
    python can't find file to pass the code to 
    there is an error with your typing and code structure  (C)
    
Question 3: what will be the output from following code print(Hello World) 

    Hello World 
    syntax error  (c)
    run-time error 
    print(Hello World)     
    

Question 4: improper indentation is an example of what type of error 

    syntax error  (C)
    run-time error 
    semantic error 
    user error 
    
Question 5: what is the output  of   the following code ? 
print("Hello"+2+"world") 

    Hello 2 world 
    TypeError  (C)
    Hello2world 
    HelloHelloworld 
'''
