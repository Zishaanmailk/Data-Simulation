# import library
import  matplotlib.pyplot as plt
import numpy as np

#ploting instance
ax=plt.axes(projection="3d")
#generate data for sin-wave
x=np.linspace(0,100,1000)
y=np.linspace(0,100,1000)+np.sin(x)
xx=np.concatenate([x,y])
xx=xx.reshape(-1,2)

#function which plot static 3d animation of sine-wave
def static():
    #loop for animation and append values to array
    for i,j in xx:
        # clears previous graph
        plt.cla()
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        ax.set_xlim(0, 110)
        ax.set_ylim(0, 110)
        ax.set_zlim(-2, 2)
        z = np.sin(j) + np.sin(i)
        ax.scatter(i,j,z)
        #delays time
        plt.pause(0.001)
    plt.show()

#function which plot dinamic 3d animation of sine-wave
def dinamic():
    # loop for animation and append values to array
    for i, j in xx:
        # clears previous graph
        plt.cla()
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        z = np.sin(j) + np.sin(i)
        ax.scatter(i, j, z)
        # delays time
        plt.pause(0.001)
    plt.show()

#calling function
static()
dinamic()