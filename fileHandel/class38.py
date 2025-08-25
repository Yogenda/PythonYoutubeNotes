# f = open('E:\\youtube tut\\fileHandel\\cam.jpg','rb')
# data = f.read()
# cpy = open('E:\\youtube tut\\fileHandel\\camcpy.jpg','wb')
# cpy.write(data)
# f.close()
# cpy.close()

# with open('text.txt','wb') as f:
#     f.write(b'abcdefghijkl')
    
# with open('my.data','wb') as f:
#     f.write('abcdefghijkl'.encode)

# with open('my.data','rb') as f:
#     print(f.read(3))
    
# with open('my.data','rb') as f:
#     print(f.read(3).decode)
    
# with open('my.data','rb') as f:
#     print(f.read(3).decode)
#     f.seek(3,1)
#     print(f.read(1).decode)

#zip /unzip
# from zipfile import *

# f= ZipFile("images.zip",'w',ZIP_DEFLATED)
# f.write('E:\\youtube tut\\fileHandel\\cam.jpg')
# f.write('E:\\youtube tut\\fileHandel\\facebook.png')
# f.write('E:\\youtube tut\\fileHandel\\html.png')
# f.write('E:\\youtube tut\\fileHandel\\instagram.png')
# f.write('E:\\youtube tut\\fileHandel\\azure.png')

# f.close()

from zipfile import *
f = ZipFile('E:\\youtube tut\\images.zip','r')
f.extractall()
f.close()




