'''
def div(a,b):
    if b!=0:
        c=a/b
        return c
    else:
        return -1

a = int(input('enter the value of A: '))
b = int(input('enter the value of B: '))
c=div(a,b)
if c==-1:
    print('value not divide by 0')
else:
    print(c)
'''
'''
def div(a,b):
    if b!=0:
        c=a/b
        return c
    else:
        raise ZeroDivisionError

a = int(input('enter the value of A: '))
b = int(input('enter the value of B: '))

try:
    c=div(a,b)
    print(c)
except:
    print('Value try to divide with 0 not possible')
'''    
''' 
print('befor try')
try:
    a = int(input('enter the value of A: '))
    b = int(input('enter the value of B: '))
    c=a//b
    print('Try block execute OK')
except ZeroDivisionError as err:
    print(err)
else: 
    print("Divide is: ",c)

print('after try-except-else')
''' 
''' 
print('befor try')
try:
    a = int(input('enter the value of A: '))
    b = int(input('enter the value of B: '))
    c=a//b
    print('Try block execute OK')
except ZeroDivisionError as err:
    print(err)
else: 
    print("Divide is: ",c)
finally:
    print('finally block')
print('after try-except-else')
'''
'''
def div(a,b):
    try:
        c=a//b
        return c
    except ZeroDivisionError as err:
        raise ZeroDivisionError
    finally:
        print('finally block')
     
z=div(4,0) 
print(z)
'''


