'''
def add(a,b,c,d,e,f):
    return a+b+c+d+e+f
r=add(2,5,9,7,6,4)
print(r)
r=add(b=2,c=5,a=9,f=7,d=6,e=4)
print(r)
'''
'''
def add(a,b, / ,c,d,e,f):
    return a+b+c+d+e+f
# r=add(a=9,b=2,c=5,f=7,d=6,e=4)
# print(r)
r=add(9,2,5,f=7,d=6,e=4)
print(r)
'''
'''
def add(a,b, / ,c,d,*,e,f):
    return a+b+c+d+e+f
r=add(9,2,5,7,f=6,e=4)
print(r)
'''
'''
def add(*,a,b):
    return a+b
r=add(b=2,a=5)
print(r)
'''
'''
def add(a, b , / c, d, e, f) 
what does alphabets before slash means in the above function ? 

    Positional Argument  (C)
    keyword Argument 
    Both Positional and keyword Argument 
    All of the Above 


What is the Default Return Value for a Function that Does not Return Any Value? 

    Integer 
    String 
    Null 
    None  (C)


What are the Items Present Inside Function Header? 

    return value 
    Result 
    Def 
    Function Name and Parameter List  (C)
'''
'''
# Variable length argumets
def fun1(*args):
    print(type(args),args)

fun1() 
fun1(1,2,3,4) 
fun1(10,20,30,40,50,60,70,80,90)
fun1('Vicky',10,70.6,5+8j)
'''
'''
def fun1(a,b,*args):
    print(a,b,args)
# fun1()
fun1(10,20)
fun1(10,20,30,40,50) 
fun1(10,20,30,40,50) 
'''
'''
def fun1(*args,a,b):
    print(a,b,args)
# fun1()
# fun1(10,20)
fun1(10,20,30,40,50,a=60,b=70) 
'''
'''
def fun1(a,b,c):
	print(a,b,c)
l=[10,20,30]
fun1(l[0],l[1],l[2])
fun1(*l)
'''
'''
def fun1(a,b,c):
	print(a,b,c)

t=(10,20,30)
fun1(*t)
str='Tea'
fun1(*str)
s={11,22,33}
fun1(*s)
'''
'''
#store multiple values in the different variable
def fun1(a,b,c):
	return a+1,b+2,c+3

x,y,z=fun1(10,20,30)
print(x,y,z)
t=fun1(1,2,3)
print(t,type(t))
'''
