'''
s1='abcd'
n = 10
f = 14.06
print(isinstance(s1,str))
print(isinstance(n,int))
print(isinstance(f,float))
print(isinstance(n,float))
'''
'''
l=[10,'abhishek','hemant',14.16]
itr= iter(l)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
'''
'''
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
m = map(lambda x:x**2, l1)
print(list(m))
m = map(lambda x,y:x+y, l1,l2)
print(list(m))
print(max(l1))
print(min(l2))
print(sum(l1))
l3=[4,9,8,3,6,7,1,2]
print(sorted(l3,reverse=True))
'''
l1=[1,2,3,4,5]
l2=['a','b','c','d','e']
z=zip(l1,l2)
print(z)
for x,y in z:
    print(x,y)
    
rev=reversed(l1)
print(next(rev), end=" ")
print(next(rev), end=" ")
print(next(rev))
print(pow(2,4))
print(round(14.1237215))