import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,11)
y=x**2

# print(x)
# print(y)

# plt.plot(x,y,'r')
# plt.plot(x,y,'p')

# plt.subplot(1,2,1)
# plt.plot(x,y,'r--')
# plt.subplot(1,2,2)
# plt.plot(x,y,'g*')

# fig=plt.figure() #******* create figure
# axes=fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y,'b')
# axes.set_xlabel('X_Label_axes')
# axes.set_ylabel('Y_Label_axes')
# axes.set_title('axes_Title')

# axes1=fig.add_axes([0.1,0.1,0.8,0.8]) #******** (main axes) add set of axes to figure left,bottom,width,height
# axes2=fig.add_axes([0.2,0.5,0.4,0.3]) #******** (inset axes)

# axes1.plot(x,y,'b') #******** plot on that set of axes 1 large figure
# axes1.set_xlabel('X_Label_axes1')
# axes1.set_ylabel('Y_Label_axes1')
# axes1.set_title('axes1_Title')

# axes2.plot(x,y,'r') #******** plot on that set of axes 2 Insert figure
# axes2.set_xlabel('X_Label_axes2')
# axes2.set_ylabel('Y_Label_axes2')
# axes2.set_title('axes2_Title')

# ************************************************
fig,axes = plt.subplots(nrows=1, ncols=2)
# axes.plot(x,y,'r')
# axes.set_xlabel('X')
# axes.set_ylabel('Y')
# axes.set_title('Title')

# for ax in axes:
#     ax.plot(x,y,'b')
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.set_title('title')

plt.show()