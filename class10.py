''' 
for i in range(0,5): #0,1,2,3,4
    for j in range(0,5): #0,1,2,3,4
        print(i,j, end='  ')
    print(' ')

* * * * *
* * * * *
* * * * *
* * * * *


for i in range(0,5): #0,1,2,3,4
    for j in range(0,5): #0,1,2,3,4
        print('*', end='  ')
    print(' ')


for i in range(0,5): #0,1,2,3,4
    for j in range(0,5): #0,1,2,3,4
        if i<j:
            print('*', end='  ')
    print(' ')


for i in range(0,5): #0,1,2,3,4
    for j in range(0,5): #0,1,2,3,4
        if i>=j:
            print('*', end='  ')
    print(' ')
'''
s1='abc'
s2='xyz'
for i in s1: 
    for j in s2: 
        print(i,j,end=' ')
    print(' ')
