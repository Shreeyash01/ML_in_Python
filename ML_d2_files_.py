# import os
# c=os.getcwd()
# print(c)

# file=open("i2it.txt",'w')
# file.close()

# try:
#     f=open("i2it.txt")
# except:
#     f.close()

# try:
#     f=open("i2it.txt")
# finally:
#     f.close()

# try:
#     f=open("i2it.txt",'w')
#     f.write('Hi! I am SAM \n Machine Learning is going on!')
# except:
#     f.close()

with open('i2it.txt','w') as f:    #*********** with closes file itself
    f.write('This is first line\n')
    f.write('This is second line\n\n')
    f.write('This is last line\n')

f=open('i2it.txt')
# f.read()
# print(f.read())
# print(f.tell())
# f.seek(0)
# print(f.tell())

# print(f.read(8))
# print(f.tell())
# print(f.read())

# f.seek(0)
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.read())

# f.seek(0)
# print(f.readlines())
# f.seek(0)
# print(f.readlines()[0])

# f.seek(0)
# for v in f:
#     print(f.read())










