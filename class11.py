'''
day = int(input('enter your day number: '))
if day==1:
    print('Sunday')
elif day==2:
    print('Monday')
elif day==3:
    print('Tuesday')
elif day==4:
    print('Wedday')
elif day==5:
    print('Thursday')
elif day==6:
    print('Friday')
elif day==7:
    print('Saturday')
else:
    print('holiday')
 

print('Press 1: US citizenship')
print('Press 2: Canada citizenship')
print('Press 3: India citizenship')
print('Press 4: Pakistan citizenship')

a=int(input('Enter your citizen number: '))
match a:
    case 1: 
        print("you got US citizenship")
    case 2: 
        print("you got Canada citizenship")
    case 3: 
        print("you got India citizenship")
    case 4: 
        print("you got Pakistan citizenship")
    case _:
        print("you are the part of ISIS")
'''

#string
'''
s="hello"
print(type(s))
s1='hello'
print(type(s1))  
s2=input("enter anything: ")
print(type(s2))
print(len(s2))

s1='Hello'
for x in s1:
    print(x, end='')
#hello
#yogendra's
s2="yogendra's"
print(s2)


s1="Hello"
s2="World"
s3=s1+s2
print(s3)
print(s1,s2)

s5="hello "+str(5)
print(s5)

s6='hello '+"how "+"are "+"you"
print(s6)

s3='hello '*3
print(s3)

s4="hello"
print(s4[-3])
s4="hello"
print(s4[1])

h1="hello world"
for i in range(0,len(h1)):
    print(h1[i])
'''