import  matplotlib.pyplot as plt
import numpy as np

x=np.linspace(1,100,1000)
y=np.linspace(1,100,1000)

x,y=np.meshgrid(x,y)
print(x.shape)
z=(x-y)*0
ax=plt.axes(projection="3d")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.plot_surface(x, y, z)
plt.show()