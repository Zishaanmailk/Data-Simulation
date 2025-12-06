# import library
import numpy as np
import matplotlib.pyplot as plt

#generate x ,y points
x=np.linspace(0.00000001,1000,999999)
y=np.log(x)
y2=np.log10(x)

#ploting log(x)
fig,ax=plt.subplots(2)

ax[0].plot(x, y, label="y=log(x)")
ax[0].set_xlabel("x")
ax[0].set_ylabel("y")
#make mid-value of x number line as 0
ax[0].axhline(0)
# make mid-value of y number line as 0
ax[0].axvline(0)
# display label for line
ax[0].legend()

#ploting log10(x)
ax[1].plot(x, y2, label="y=log10(x)")
ax[1].set_xlabel("x")
ax[1].set_ylabel("y")
#make mid-value of x number line as 0
ax[1].axhline(0)
# make mid-value of y number line as 0
plt.axvline(0)
# display label for line
ax[1].legend()

# display graph
plt.show()


