from threading  import *
from time import *
# class Alph(Thread):
# def display():
#     for i in range(65,91):
#         print(chr(i),end=" ")
#         sleep(0.5)

# t= Thread(target=display, name="Alpha")
# t.start()
# for i in range(65,91):
#     print(chr(i),end=" ")
#     sleep(0.5)
# t.join()
'''
class Alphabet(Thread):
    def run(self):
        for i in range(65,91):
            print(i)
            sleep(1)
t=Alphabet()
t.start()   
for i in range(65,91):
    print(i)
    sleep(1)         
t.join()
'''
'''
def display(str1):
    for x in str1:
        print(x)

t1 = Thread(target=display, args=('Hello world',))
t2 = Thread(target=display, args=('How are you all',))

t1.start()
t2.start()

t1.join()
t2.join()
'''
'''
def display(str1):
    l.acquire()
    for x in str1:
        print(x)
    l.release()

l=Lock()

t1 = Thread(target=display, args=('Hello world',))
t2 = Thread(target=display, args=('How are you all',))

t1.start()
t2.start()

t1.join()
t2.join()
'''

def display(str1):
    l.acquire()
    for x in str1:
        print(x)
    l.release()

l=Semaphore(1)

t1 = Thread(target=display, args=('Hello world',))
t2 = Thread(target=display, args=('How are you all',))
t3 = Thread(target=display, args=(' We are learning python',))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()