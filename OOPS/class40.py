# class Rectange:
#     def __init__(self,length,bredth):
#         self.length = length
#         self.bredth = bredth
    
#     def area(self):
#         return self.length * self.bredth
    
#     def param(self):
#         return 2*(self.length+self.bredth)

# r1= Rectange(10,5)
# print(r1)

'''
# inside the constructor
class Test:
    def __init__(self):
        self.a = 10
t = Test()
print(dir(t))
'''   
'''
# method inside the class
class Test:
    def __init__(self):
        self.a = 10
        
    def fun(self):
        self.b =20
t = Test()
t.fun()
print(dir(t))
'''
'''
# Outside the method
class Test:
    def __init__(self):
        self.a = 10
        
    def fun(self):
        self.b =20
t = Test()
t.fun()
t.c=30
print(dir(t))
'''
'''
class Test:
    def __init__(s):
        s.a = 10
        
    def fun(s):
        s.b =20
t = Test()
t.fun()
t.c=30
print(dir(t))
'''
