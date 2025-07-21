'''
l1=[1,2,3]
l2=[7,8,9]
# print(l1+l2)
# l3 = l1+l2
# print(l3)
# print(l1+[4])
# print(l1)
# print(l2)
l1.extend(l2)
l1.extend([14,15,16])
# print(l1)
# print(l2)
# l2=l2+[10,11,12]
# print(l2)
# l3=[6,7,8]
# print(l3*3)
# print(l3*2.5)
print(l1)
print(1 in l1)

if 3 in l1:
    print("found")
else:
    print("Not found")

print(5 not in l1)  
print(5 in l1)
print(14 not in l1)'''
'''
l1=[6,7,8,9,10]
# print(l1[4])
for x in l1:
    print(x)
'''
'''
l1=[6,7,8,9,10]
# print(len(l1))
for y in range(len(l1)):
    print(l1[y],end=' ')
print('')
#01 9, 8 ,7 ,6 
for x in range(len(l1)-1,-1,-1):
    print(l1[x], end=' ')
    '''

# l1=[6,7,8,9,10]   
# i=0
# while i<len(l1):
#     print(l1[i], end=' ')
#     i=i+1
    
'''
l2=[6,7,8,9,10]
i=len(l2)-1
while i>=0: 
    print(l2[i]) 
    i=i-1
'''
'''
l1=[9,8,7,6,5,4,3]
print(len(l1))
l1.append(6)
print(len(l1))
print(l1)

l1[len(l1):]=[10]
print(l1)
l1[5:5]=[20]
print(l1)
'''

l1=[5,6,7,8,9]
l1.extend([10,11,12])
print(l1)
l1.extend('hemant')
print(l1)
