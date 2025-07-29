'''
dict1={101:'pranshu',102:'Abhishek',103:'Madu',104:'Deepak'}
print(type(dict1))
print(dict1[101])
dict1[105]='Aniket'
print(dict1)
del dict1[104]
print(dict1)
'''
'''
dict2={101:'pranshu',102:'Abhishek',103:'Madu',104:'Deepak'}
# for i in dict2:
#     print(i)
for i in dict2:
    print(i,dict2[i])
'''
'''
dict2={101:'pranshu',102:'Abhishek',103:'Madu',104:'Deepak'}
dict3 = dict()
print(type(dict3))
print(dict3)
# dict3['Red']='Apple'
# dict3['Yellow']='Mango'
#1:1,2:4
for x in range(1,6):
    dict3[x]=x**2
print(dict3)
'''
'''
dict2 = dict(((1, 1), (2, 4), (3, 9), (4, 16), (5, 25)))
print(dict2)
dict3 = dict(([1, 1], [2, 4], [3, 9], [4, 16], [5, 25]))
print(dict3)
dict4 = dict(('ab','cd','ef'))
print(dict4)
# dict5 = dict(([1, 1,11], [2, 4,22], [3, 9,44], [4, 16,33], [5, 25,55]))
# print(dict5)
l=[(1,2),(3,4),(5,6)]
d2=dict(l)
print(d2)
print(type(d2))'''
'''
l1=['A','B','C']
l2=['Apple','Ball','Cat']
d1=dict(zip(l1,l2))
print(d1)
s1={7,8,9}
str1='abc'
d2 = dict(zip(s1,str1))
print(d2)
'''
'''
#if value exciede then it will skip the other values
d3=dict(zip([10,20,30],(101,102,103,104,105)))
print(d3)
'''
#enumerater
'''
l1=['a','b','c']
for item in enumerate(l1):
    print(item)

d1=dict(enumerate(l1))
print(d1)
print(type(d1))
'''
'''
d4={x:x**2 for x in range(1,5)}
print(d4)
d5={(x,x**2) for x in range(1,5)}
print(d5)
print(type(d5))
'''
