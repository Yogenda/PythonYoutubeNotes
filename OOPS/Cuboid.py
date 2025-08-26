''' 
class Cuboid:
    # constuctor
    def __init__(self,l,b,h):
        print(id(self))
        self.length = l
        self.bredth = b
        self.height = h 
            
    def area(self):
        return self.length * self.bredth
    def vol(self):
        return self.length*self.bredth*self.height
    def totalSurf(self):
        return 2*(self.length * self.bredth + self.bredth*self.height + self.length*self.height)
    
c1 = Cuboid(20,10,2) 
print(id(c1))
print(c1.area())
c2 = Cuboid(2,3,4)
print(id(c2))
print(c2.vol())
c3 = Cuboid(2,3,4)
print(id(c3))
print(c3.totalSurf())
'''
class Cuboid:
    def __init__(self,l=1,b=1,h=1):
        print(id(self))
        self.length = l
        self.bredth = b
        self.height = h 
            
    def area(self):
        return self.length * self.bredth
    def vol(self):
        return self.length*self.bredth*self.height
    def totalSurf(self):
        return 2*(self.length * self.bredth + self.bredth*self.height + self.length*self.height)

c1 = Cuboid()
c2 = Cuboid(10)
c3 = Cuboid(10,5)
c4 = Cuboid(10,5,3)



        
       
    