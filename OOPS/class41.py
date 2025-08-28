'''
class Rectange:
    count=0 
    def __init__(self,length,bredth):
        self.length = length
        self.bredth = bredth
        Rectange.count += 1
    
    def area(self):
        return self.length * self.bredth
    
    def param(self):
        return 2*(self.length+self.bredth)
    
    @classmethod
    def countRect(cls):
        print(cls.count)
    
r1 = Rectange(10,20)
r1.countRect()
'''
'''
class Rectange:
    def __init__(self,length,bredth):
        self.length = length
        self.bredth = bredth
    
    def area(self):
        return self.length * self.bredth
    
    def param(self):
        return 2*(self.length+self.bredth)
    
    @staticmethod
    def issquare(len, bre):
        return len==bre
        
r1= Rectange(10,5)
print(r1.issquare(10,10))
print(Rectange.issquare(10,20))
'''

class Rectange:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
    def getLength(self):
        return self.length
    def setLength(self,l):
        self.length=l
    def area(self):
        return self.length * self.breadth
    def param(self):
        return 2*(self.length+self.breadth)

r=Rectange(10,5)
print(r.getLength())
r.setLength(50)
print(r.getLength())
print(r.area())

  