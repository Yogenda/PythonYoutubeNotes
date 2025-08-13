'''
# chr: it will give you the character value of an ASCII code.
print(chr(65))
# ord: it will take an char and give its ASCII code.
print(ord('A'))

print(divmod(11,3))
p,q=divmod(11,3)
print(p)
print(q)

l=[10,20,30,40,50,60]
e = enumerate(l)
print(e)
for i in e:
    print(i)

print('3*10+15/3')
print(eval('3*10+15/3'))
print(eval('Hemant')) #error

s='x=10\ny=20\nprint(x+y)'
print(exec(s))
'''
''' 
l=[3,6,7,9,12,14,15,16,21]
def even(x):
    if x%2==0:
        return True
    else:
        return False
f= filter(even,l)
for i in f:
    print(i)

f = filter(lambda x:x>10,l)
for i in f:
    print(i)

 '''
 
# f='c'
# print(format(f,'c'))
# print(type(f))

l=[1,2,3,4,5,6]
fz=frozenset(l)
print(fz)

s1='abcde'
print(hasattr(s1, 'lower'))
print(hasattr(s1, 'upper'))
print(hasattr(s1, 'total'))

n=10
print(hash(n))
f=12.25
print(hash(f))

s1='abcde'
print(help(s1.lower))
print(help(s1.isdigit))