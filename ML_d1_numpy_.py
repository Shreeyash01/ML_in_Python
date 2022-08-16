import numpy as np
l1=[1,2,3,4,5]
# print(type(l1))
# print(l1)

a1=np.array(l1)
# print(type(a1))
# print(a1)
# print(a1.shape)

s='asdghgjk'
# print(s[-2:-6:-1])

l2=[[1,2,3],[4,5,6],[7,8,9]]
# print(type(l2))
# print(l2)

a2=np.array(l2)
# print(type(a2))
# print(a2)
# print(a2.shape)

l3=list(range(1,26))
# print(l3)
a3=np.array(l3)
# print(a3)
a4=a3.reshape(25,1)
# print(a4)

#******** only for ones and zeros
a5=np.zeros(10)
# print(a5)
a6=np.ones(10)
# print(a6)
#********* for other vals
a7=np.zeros(10)+5
# print(a7)
a8=np.ones(10)*8
# print(a8)

a9=np.zeros((5,10))+9
# print(a9)
a10=np.zeros((5,10),dtype=int)+9
# print(a10)

a11=np.eye(10,dtype=int) #**** Indentity Matrix
# print(a11)

b1=np.random.rand(10) #****** Uniform distribution
# print(b)

b2=np.random.rand(5,5) #****** Uniform distribution
# print(b2)

b3=np.random.randn(10) #****** Standard normal (+ve/-ve vals) distribution
# print(b3)

b4=np.random.randint(5) #****** int in range(0,5)
# print(b4)

b5=np.random.randint(10,20,6)
# print(b5)
b6=np.random.randint(10,20,6).reshape(2,3)
# print(b6)

b7=np.linspace(10,100,5) #******
# print(b7)

b8=np.arange(1,26).reshape(5,5)
# print(b8)
# print(b8[3][4])
# print(b8[3:4,4:5])
# ****** Adj data
# print(b8[2:3,2:4])
# print(b8[0:3,1:2])
# print(b8[3:5,0:5])
# print(b8[3:,0:])
# print(b8[2:4,1:4])
# ****** UnAdj data
# print(b8[[0,4],[0,4]])
# print(b8[[0,3],[1,3]])
# print(b8[[0,3],[3,1]])

# print(b8[0:5,0:1].sum())
print(b8.sum(0)) # *** for cols sum
print(b8.sum(1)) # *** for rows sum
print(b8.sum(axis=1))