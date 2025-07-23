'''
l1=[]
print(l1)
for x in range(10):
    l1.append(x)
print(l1)
'''
'''
l1=[x for x in range(10)]
print(l1)

l1=[x**2 for x in range(1,6)]
print(l1)

l1=[x for x in (10,5,9,8,7,3,4,15,21,46,98,32) if x%2==0]
print(l1)

l1=[x.lower() for x in 'CodINg']
print(l1)

l1=[x for x in 'abc^$%123jutest87#)' if x.isalpha()]
print(l1)

data = [input("Enter your names: ").split()]
print(data)
'''
'''
Quiz:
Question 1: What is the Output of the Following 
list1=[None]*10 
print(len(list1)) 

    0 
    error 
    10          (c)
    None repeats 10 times 


Question 2: How can we modify the following list 
MyList=[10, 20, 30, 40] 

    MyList.append[50]  
    MyList.append(50) (c)
    extend.myList[50] 
    mylist.extend(50) 


Question 3: Which of the following statement is invalid ? 
list1 = [1, 2, 3] and list2 = [4, 5, 6] are given 

    list1 + list2 
    list1 *5 
    list1.extend(list2) 
    list2 * 2.5  (c)


Question 4: Which of the Following Code is not for 
reversing order of Names ? 
Names = [ 'Bob ' , 'Peter' , 'Jack' , 'Jackson' , 'Harry' ] 

    Names[-1 : -6 : -1] 
    Names.reverse( ) 
    Names[ : :-1] 
    Names[-1 : -6 : 1]  (c)


Question 5: What is the Output of the Following Code 
list =[ 1 , [2,3,] ,4  , 5 , [6,7] ,[ 8 ,9] ,10 ] 
list[5] 

    10 
    (6, 7) 
    [8, 9]  (c)
    [ [2,3,][6,7][ 8 ,9] ] 


Question 6: What is the Output of the Following Code 
l=[1,2,3,4,5] 
l[1:3]=[7,8,9] 

    [1, 7, 8, 9, 4, 5]  (c)
    [1, 2, 3,7, 8, 9, 4, 5] 
    [ 1, 2 , 3, 4, 5, 6 , 7 , 8 , 9 ] 
    [ 7, 8, 9 ] 


Question 7: What will be the Output of the Following Code 
l =['python ', 'is', 'a', 'userfriendly', 'programming', 'language'] 
l[0:6:2] 

    [ 'python ', 'is', 'a', 'userfriendly', 'programming' ] 
    [ 'python ', 'userfriendly', 'programming',  'language' ] 
    [ 'python ', 'a', 'programming' ] (c)
    [  'python ', 'is', 'a', 'programming'] 
'''

t1=('Yogendra', 123, 1.50, 5+6j,'Yogendra',45)
print(t1)
print(type(t1))
print(t1[2])
# t1[2]=85
# print(t1)
t1=(1,2,3,4,5,6)
print(t1)
t2=()
print(t2)
print(type(t2))
t3=(10)
print(type(t3))
t3=(10,)
print(type(t3))
t4=tuple((1,2,3,4,5,6))
print(t4)
print(type(t4))
t5=tuple([1,2,3,4,5,6,7])
print(t5)
print(type(t5))
t6=tuple('Abhishek')
print(t6)
print(type(t6))
t7=tuple((1,2,3))
print(t7)
print(type(t7))
