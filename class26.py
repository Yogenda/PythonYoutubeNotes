'''
d1={101:'pranshu',102:'Abhishek',103:'Madu',104:'Deepak'}
for x in d1:
    print(x,d1.get(x))

print(d1[101])
print(d1.get(101)) 
# print(d1[105])
# print(d1.get(105))
print(d1.get(105,'No studnet'))
'''
'''
d1={101:'Pranshu',102:'Abhishek',103:'Madu',104:'Hemant'}
print(d1.keys())
print(d1.values())
print(d1.items())

for k in d1.keys():
    print(k,d1[k])
for k in d1.values():
    print(k)
for l,m in d1.items():
    print(l,m)
'''
'''
d1={101:'Pranshu',102:'Abhishek',103:'Madu',104:'Hemant'}
d2 = d1.copy()
print(id(d1))
print(id(d2))
print(id(d1[101]))
print(id(d2[101]))
print(d1)
print(d2)
'''
'''
d1={101:'Pranshu',102:'Abhishek',103:'Madu',104:'Hemant'}
d2={106:'Ashraf',107:'Abhi'}
d1.update(d2)
print(d1)
print(d1.get(102))
print(d1.get(110))
print(d1.setdefault(110))
print(d1.get(110))
print(d1)
print(d1.setdefault(111,'new std'))
print(d1)
'''
'''
l1=[10,11,12,13,14]
d1={}
print(d1.fromkeys(l1))
print(d1.fromkeys(l1,101))
print(d1.fromkeys(l1,'hello'))
'''
'''
d1={101:'Pranshu',102:'Abhishek',103:'Madu',104:'Hemant'}
print(d1.pop(103))
print(d1)
# print(d1.pop(103))
print(d1.pop(110,'None'))
print(d1)
print(d1.popitem())
# print(d1.popitem(101))
d1.clear()
print(d1)'''
'''
which of the following condition is True 

    Dictionaries are immutable 
    Any  Data Type can be used for Keys 
    Dictionaries are Accessed by keys  (C)
    Dictionaries are functions 
    
D = dict() 
for x in enumerate(range(2)): 
D[x[0]] = x[1] 
D[x[1]+7] = x[0] 
print(D) 

    {0: 1, 7: 0, 1: 1, 8: 0} 
    {0: 0, 7: 0, 1: 1, 8: 1} (C)
    {1: 1, 7: 2, 0: 1, 8: 1} 
    KeyError 


What is the output of the following Code? :- 
a = {i: i * i for i in range(6)} 
print (a) 

    Dictionary comprehension doesn’t exist 
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6:36} 
    {0: 0, 1: 1, 4: 4, 9: 9, 16: 16, 25: 25} 
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25} (C)


What Will be the Output of the Following Code 
d={1:'foo', 2:'boo', 3:'doo'} 
del d[2] 
d[2]='m' 
del d[3] 
len(d) 

    Error
    0 
    1 
    2 (C)
    

What will be the Output of Following Code 
summer = {"fruit" : "mango", "juice" : "cool drinks","hobby" : "swimming"} 
for n in summer : 
    print(n) 

mango 
cool drinks 
swimming 

"fruit":"mango" 
"juice":"cool drinks" 
''hobby":"swimming" 

fruit 
juice       (C)
Hobby 

["fruit":"mango", "juice":"cool drinks", ''hobby":"swimming"] 




Methods on which a Dictionary Can Perform Looping 

    key(), value(), item()  (C)
    copy(), del(), update() 
    pop(), clear(), none 


What will be the Output of Following Code 
x = {2: 6, 3: 9, 5: 10} 
x.pop(3) 
x 

    {2:6, 3:9} 
    {} 
    {2: 6, 5: 10}  (C)
    {2:6} 


What will be the Output of Following Code 
s = {1: 'A', 2: 'B', 3: 'C'} 
p = s.copy() 
p[2] = "D" 
print(p) 

    {1:'A',  2:'B', 3:'C'} 
    {1: 'A', 2: 'D',3: 'C'} (C)
    Error 
    not possible 

'''