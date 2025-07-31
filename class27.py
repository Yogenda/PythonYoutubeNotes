''' 
def add(a,b,c):
    sum = a+b+c
    # print(sum)
    return sum

# add(10,20,30)
print(add(10,20,30))
r= add(10,20,30)
print(r)
'''
'''
def add1(a,b,c):
    print('inside a function',id(a),id(b),id(c))

x,y,z=10,15,20
print('outside a function',id(x),id(y),id(z))

add1(x,y,z)
'''
'''
# positional arguments
def sal_per(basic, allowance, deduction):
    net = basic+allowance-deduction
    return net

print('net salary is: ', sal_per(8000, 2000, 1000))

# keyword arguments
def sal_per(basic, allowance, deduction):
    net = basic+allowance-deduction
    return net

print('net salary is: ', sal_per(deduction=1000,basic=9000,allowance=3000))


def sal_per(basic, allowance, deduction):
    net = basic+allowance-deduction
    return net

print('net salary is: ', sal_per(9000,deduction=1000,allowance=3000))
'''
'''
def add(a,b=0,c=0): 
    return a+b+c

print(add(10,20))

def add(a,b=0,c=0): 
    return a+b+c

print(add(10,20,c=10))
'''
'''
def addItem(item, l=[]):
    l.append(item)
    return l

# l1=[1,2,3,4,5]
# print(addItem(20,l1))
# print(l1)
print(addItem(10))
print(addItem(20))
print(addItem(30))

l1=[1,2,3,4,5]
print(addItem(6,l1))
print(l1)
'''
