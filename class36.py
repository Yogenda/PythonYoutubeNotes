'''
class MyError(Exception):
    pass

try:
    raise MyError('My Error is here')
except MyError as me:
    print(me)
'''
'''
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
    
try:
    raise MyError('My Error is here')
except MyError as me:
    print(me)
    '''
'''
try:
    a=int(input("enter the first vale: "))
    try:
        b=int(input("enter the second vale: "))
        try:
            c=a//b
            print(c)
        except ZeroDivisionError:
            print('try not to divide with 0')
    except ValueError:
        print('This is value Error for b')
except ValueError:
    print('This is value Error for a')
'''

'''
Question 1: What type of error is raised when a built-in function is 
given with invalid data type values? 

    Value Error  (C)
    Type Error 
    Syntax Error 
    None 

Question 2: 
n=10 
d=0 
try: 
   k = n / d 
   print(k) 
except(ZeroDivisionError): 
   print("can't divide by zero") 
finally: 
   print("Looking good") 

    it will print. if there was an error in the function 
    it will print 'looking good' whether or not there was an error  in the function (C)
    it will on return 'looking good' to the developer in his developing console 
    it will only print 'looking good' in the case of a zerodivisionerror 


Question 3: which of the following syntax is correct 

try: 
except: 
try: 
except: 

try: 
   except: 
try: 
except: 

TRY: 
    EXCEPT: 
TRY 
   EXCEPT: 

try: 
   try: 
   except:  (c)
except: 


Question 4: What does the following code returns? 
'1' == 1 

    True 
    False  (2)
    Type Error 
    a ValueError occurs 
 

'''  