'''
t1=('Yogendra', 123, 1.50, 5+6j,'Yogendra',45,True)
print(t1[-1])
print(t1[:])
print(t1[2:])
'''
'''
quiz

How to access value 20 from the following code 
T = (‘python',[10,20,30],(40,50)) 

    T[1:2][1] 
    T[1:2](1) 
    T[1](1) 
    T[1][1] (c)

What is the Output of the Following Code 
T = ('red','green','blue',10,20,30,40,50) 
print(T[2:5], T[:4], T[3:]) 

    ('blue', 10, 20) ('red', 'green', 'blue', 10) (10, 20, 30, 40, 50) (C) 
    (‘red’,’green’,’blue’)(10,20,30,40,50) 
    [(red’,’green’,'blue',10,20,30,40,50)] 
    red','green','blue',10,20,30,40,50


Which of the Following Methods Work Both in Lists and Tuple? 

    reverse() 
    sort() 
    append() 
    pop() 
    index()  (c)


When can we use a tuple over list ? 

    For a list of items that want to use strings as key values instead of integers 
    For a list of items that will be extended as new items are found 
    For a temporary variable that you will use and discard without modifying  (c)
    For a list of items you intend to sort in place 



what will be the output of the following code 
T = (1,2,3,4,5,6,7,8,9) 
[T[i]for i in range(0, len(T),2) ] 

    [1, 3, 5, 7, 9]     (c)
    [1,2,4,6,8] 
    [1,2,3,4,5,6,7,8,9] 
    len= 8 
'''
######################SET######################
'''
s1={1,2,3,5.7,'hemant',7.8,True,'Abhi','hemant'}
print(s1)
# print(s1[1])
print(type(s1))
s2=set((1,2,3,4))
print(s2)
print(type(s2))
s3=set('Ayush')
print(s3)
print(type(s3))
'''
'''
s4={10,20,30,40,50}
print(s4)
# s4[0]=35
# print(s4)
s4.discard(50)
print(s4)
s4.add(100)
print(s4)
s4.add(120)
print(s4)
print(len(s4))
'''
s5={5,10,21,15,3,11}
print(s5)
s6={10,20,30,40,50,60,70}
print(s6)
s6.add(18)
print(s6)