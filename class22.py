'''
t1=('Yogendra', 123, 1.50, 5+6j,'Yogendra',45)
print(t1)
print(type(t1))
print(t1[2])
# t1[2]=80
# print(t1)
t1=(1,2,3,4,5,6)
print(t1)
t2=()
print(t2)
print(type(t2))
t3=(10)
print(t3)
print(type(t3))
t3=(10,)
print(t3)
print(type(t3))
t4=tuple((1,2,3,4,5,6))
print(t4)
print(type(t4))
t5=tuple([1,2,3,4,5,6])
print(t5)
print(type(t5))
t6=tuple('Comfoxy')
print(t6)
print(type(t6))
t7=tuple((1,2,3,4,5,6,7,8))
print(t7)
'''
'''
t1=10
print(t1)
print(type(t1))
t1=10,20,30,40
print(t1)
print(type(t1))
a,b,c,d=t1
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
'''
'''
l1=[1,2,3]
print(l1)
print(type(l1))
a,b,c=l1
print(a)
print(b)
print(c)
a,b,c='TEA'
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
'''
'''
t1=10,20,30,40,50
print(t1)
# a,b,c=t1
a,b,*c=t1
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
'''
'''
l1=[x for x in range(10)]
print(l1)
t1=(x for x in range(10))
print(t1)
t1=tuple(x for x in range(10))
print(t1)
t2=(*(x for x in range(10)),)
print(t2)
t3=(*(x for x in range(1,10,2)),)
print(t3)
t4=(*(x for x in 'Hemant'),)
print(t4)
'HeMAnt' 'ent'
t5=(*(x for x in 'HeMAnt' if x.islower()),)
print(t5)
t6=tuple(x**2 for x in (1,3,5,7))
print(t6)
t7=(1,2,3,4,5,6,7,4,5,6)
print(t7.count(5))
print(t7.index(5))
print(t7.index(10))
'''
t1=('Yogendra', 123, 1.50, 5+6j,'Yogendra',45,True)
# print(t1)
# for x in t1:
#     print(x)

# for i in range(len(t1)):
#     print(t1[i])
print(t1[1])

t1[2]='comfoxy'
print(t1)
