'''
a={1,2,3,4,5,7}
b={5,7,9,10,11}
print(a.union(b))
print(b.union(a))
print(a)
print(b)
'''
'''
a={1,2,3,4,5,7}
b={5,7,9,10,11}
print(a.intersection(b))
print(b.intersection(a))
'''
'''
a={1,2,3,4,5,7}
b={5,7,9,10,11}
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
'''
'''
a={1,2,3,4,5,6,7,8,9,10}
b={1,2,3,5,7}
c={4,6,8,10}
print(b.issubset(a))
print(a.issubset(b))
print(a.issuperset(b))
print(b.issuperset(a))
print(c.isdisjoint(b))
'''
# print(dir(set))
'''
s1={10,20,30,40,50}
print(s1)
s1.add(60)
print(s1)
# s1.add(70,80)
# print(s1)
s1.add((70,80))
print(s1)
s1.add(50)
print(s1)
s2=s1.copy()
print(s2)
'''
'''
s1={10,20,30,40,50}
s1.update({40,50,60})
print(s1)
s1.update((1,2,3))
print(s1)
s1.update('Coding')
print(s1)
'''
'''
s1={10,20,30,40,50}
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)
'''
'''
s1={10,20,30,40,50}
s1.discard(30)
print(s1)
# s1.remove(30)
# print(s1)
s1.discard(60)
print(s1)
# s1.remove((50,20))
# print(s1)
'''
'''
Which will create empty set 

    { } 
    ( ) 
    set( )  (c)
    [ ] 


What will be the output of num=set([1,2,3,4,2,3,4,3,2]) 
print(len(num)) 

    4  (c)
    error 
    9 
    8 


What will be the output for 
a={1,2,3} 
b=a.copy() 
b.add(4) 
print(b) 

    error 
    {1,2,3} 
    {1,2,3,4} (c)
    error , copying of set isn't allowed 


What will be the output for this program 
a={1,2,3} 
a.intersection_update({2,3,4,5}) 
a 

    error 
    {2,3} (c)
    {1,4,5} 
    error , duplicate items are present in a list 


Which of the following is not the correct syntax for creating a set 

    set([1,2,3,4]) 
    set([1,2,2,3,4]) 
    {1,2,3,4} 
    set([[1,2],[3,4]])  (c)
    
    
Which method deletes the specified element of a set and no error 
is raised if the element doesn't exist?. 

    remove 
    pop 
    dispose 
    discard (c)


'''
