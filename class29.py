'''
def fun1(**kwargs):
    print(kwargs)
fun1(name="Rahul",rollNo=25, address="delhi")

def fun1(**kwargs):
    for x in kwargs:
        print(x,kwargs[x])
fun1(name="Rahul",rollNo=25, address="delhi")

def fun1(a,b,*args,**kwargs):
    print(a,b,args,kwargs)

fun1(2,4)
fun1(2,4,name="abhishek")
fun1(2,4,20,40,name="abhishek")
'''
"""
# iterator
l=[1,2,3,4,5]
i = iter(l)
print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))
"""
'''
def Days():
    l = ['mon','tue','wed','thus','fri','sat','sun']
    i=0
    while True:
        x = l[i]
        i=(i+1)%7
        yield x

d = Days()
print(next(d),end=' ')
print(next(d),end=' ')
print(next(d),end=' ')
print(next(d),end=' ')
print(next(d),end=' ')
print(next(d),end=' ')
print(next(d))
'''
'''
a=10
print('outside',a)
def fun1(x,y):
    z=x+y
    print('local',z)
    print('global',a)

fun1(4,1)
'''

a,b,c,d=11,22,33,44
def fun1(a=10,b=20):
    x,y,z=1,2,3
    print(locals())

fun1()
print(globals())

    
