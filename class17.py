'''
s = 'A'
print(ord(s))
s = ' '
print(ord(s))
print(chr(48)) 


s='\u03b1'
print(s)
s='\u03b1\u03b2\u03b3'
print(s)
s='\u0041'
print(s)
s='\u0915\u0916\u0917'
print(s)

print('abcde\nfghijklmn',end='-')
print('abcde\ffghijklmn',end='--')
print('abcde\rfghijklmn')
print('abcde\tfghijklmn')
print('abcde\afghijklmn')
print('abcde\\fghijklmn')

print('yogendra\'s')
print('yogendra\"s')

s='\N{dollar sign}'
print(s)
s='\N{pound sign}'
print(s)
s='\N{rupee sign}'
print(s)
s='\N{Yen sign}'
print(s)
s='\N{Copyright sign}'
print(s)
s='\N{latin small letter j}'
print(s)

a=10
b='Abjishek'
c=14.05
print(a)
print(b)
print(c)
print(a,b,c)
print('hello','world')
print('hello'+'world')
print(a,b,c,sep=',')
a=10
b='Abjishek'
c=14.05
print(a, end='|')
print(b, end='|')
print(c)
rollno= 10
name = 'Abhishek'
avg = 50.49

print('Student Name is %s, his roll number is %d and the average is %f'%(name,rollno,avg))
print('studnet name is %s'%name)
print('studnet name is %10s'%name)
print('studnet average is %2.2f'%avg)'''

a=22
b=7
c=a/b
d=a+b
print('Division of {0} and {1} is {2}'.format(a,b,c))
print('addition of {0} and {1} is {3}'.format(a,b,c,d))

