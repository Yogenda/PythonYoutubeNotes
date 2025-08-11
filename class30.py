# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)

# r = fact(5)
# print(r)

'''
def f(): 
   global a 
   print(a) 
   a = "hello" 
   print(a) 
a = "world" 
f() 
print(a) 
'''
'''
What is the  Advantage of using local variables? 

    They Allow the Variable to be Used Throughout the program 
    They Allow Variable Identifiers to be Reused Each Time   (C)
    They are Easier to Program than Global Variables 
    A Wider Range of Data Types can be Used 


What is the Output of the Following Code 
def f(): 
   global a 
   print(a) 
   a = "hello" 
   print(a) 
a = "world" 
f() 
print(a) 

hello 
hello 
world 

world 
hello     (C)
hello 

world 
hello 
world 



What will be the Output of the Following Code 
def f1(): 
   x = 15 
   print(x) 
x = 12 
f1() 

    Error 
    12 
    15  (c)
    1512 
'''
'''
# abs() : provide the absolute value if number is +ve it return +ve and if nubmer is -ve 
# it returns +ve
a = -5
print(abs(a))
b = -5.89
print(abs(b))
'''

# ASCII(): it convert the code into ascii value
print(ascii(5))

c= '\u0521'
print(c)
print(ascii(c))

#bin: it will conver the number into binary form.
#bool(): it will conver the datatype into boolean.

#bytearray() and bytes() are same.
# bytearray(): it will create the array of byte. this is mutable.
# bytes(): this is non mutable
d = bytearray(10)
print(d)
s1= 'abcd'
# h= bytearray(s1)
# print(h)
s3=bytearray(s1.encode())
print(s3)
for i in s3:
    print(i)
    
a= s3.append(101)
# b= bytes(s1)

# callable(): it will check the value in function or not. 
# if it is a function it will return true else false.
def add(a,b):
    return a+b
s1 ='abcd'
n = 10
print(callable(s1))
print(callable(n))
print(callable(add))