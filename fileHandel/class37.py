'''
file=open('E:\\youtube tut\\fileHandel\\MyData.txt','r')
str1=file.read()
print(str1)
'''
'''
file=open('E:\\youtube tut\\fileHandel\\MyData.txt','r')
str1=file.read(10)
print(str1)
file.close()
'''
'''
#Write method
file=open('E:\\youtube tut\\fileHandel\\Write.txt','w')
file.write("Hello friends")
file.write("\nhow are you all")
file.write("\ni hope you are good")
file.close()
'''
'''
file=open('E:\\youtube tut\\fileHandel\\Write.txt','a')
file.write("\nHello Humera, Hemant")
file.write("\nhow are you both")
file.write("\ni hope you are good")
file.close()
'''
'''
file=open('E:\\youtube tut\\fileHandel\\Write.txt','r+')
str1= file.read()
print(str1)
file.write("\nWe are learning pyhton in this class")
file.write("\ni hope you are learning it well")
file.close()
'''
'''
file= open('E:\\youtube tut\\fileHandel\\MyData.txt','r')
print(type(file))
file= open('E:\\youtube tut\\fileHandel\\MyData.txt','wb')
print(type(file))
# print(dir(file))
file= open('E:\\youtube tut\\fileHandel\\MyData.txt','w')
print(type(file))
# print(dir(file))

file= open('E:\\youtube tut\\fileHandel\\MyData.txt','r')
print(file.close())
print(file.name)
print(file.mode)
print(file.closed)
'''
'''
file= open('E:\\youtube tut\\fileHandel\\MyData.txt','r')
# line= file.read()
# print(line)
# line= file.readline()
# print(line)
line= file.readlines()
print(type(line))
'''
'''
file= open('E:\\youtube tut\\fileHandel\\MyData.txt','r')
lines= file.readlines()
for line in lines:
    print(line,end='')
'''
'''
file= open('E:\\youtube tut\\fileHandel\\MyData.txt','w')
str1='we are learning python from 0\nto become an hero\nand will learn dsa'
file.write(str1)
'''
file= open('E:\\youtube tut\\fileHandel\\MyData.txt','w')
str1=['we are learning python from 0\nto become an hero\nand will learn dsa\n']
file.writelines(str1)
