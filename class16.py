'''
s = 'hello students how are you all'
# s = 'Python is very easy'
result = s.partition('e')
print(result)
print(type(result))
result = s.rpartition('e')
print(result)
print(type(result))


s='a-b-c-d-e-f'
print(s)
print(s.replace('-',','))
print(s.replace('-',',',3))
print(s.replace('f','z'))

# abc@yahoo.com
# abc@hotmail.com

email = 'abc@yahoo.com'
print(email.replace('yahoo.com','hotmail.com'))

s1='xyz'
s2='abc'
#axyzbxyzc
print(s1.join(s2))
s3='/'
# a/b/c
print(s3.join(s2))
l1=['abhishek','deepak','komal']
s4='-'
# abhishek-deepak-komal
print(s4.join(l1))
s4=','
# abhishek,deepak,komal
print(s4.join(l1))

name='vishal abhishek deepak'
s=name.split()
print(type(s))
print(s)
print(name.split('a'))
name='vishal-abhishek-deepak'
print(name.split('-',1))
name='vishal-abhishek-deepak-Yogendra'
print(name.rsplit('-'))
print(name.rsplit('-',2))

s='aaa\nbbb\tccc\rddd\feee'
print(s.splitlines())
print(s.splitlines(keepends=True))'''

