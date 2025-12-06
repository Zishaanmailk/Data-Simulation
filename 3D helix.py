# import library
import  matplotlib.pyplot as plt
import numpy as np
#ploting 3D
ax=plt.axes(projection="3d")
x=np.linspace(0,100,10000)
y=np.sin(x)
 #x,y=np.meshgrid(x,y)
z= np.cos(x)
ax.plot(x,y,z)
plt.show()
