# import library
import numpy as np
import matplotlib.pyplot as plt

#generate x ,y points
x=np.linspace(-1000,1000,999999)
y=np.exp(x)

#ploting
plt.plot(x, y, label="y=exp(x)")
plt.xlabel("x")
plt.ylabel("y")
#make mid-value of x number line as 0
plt.axhline(0)
# make mid-value of y number line as 0
plt.axvline(0)
#set yaxis range
plt.ylim(-2, 10)
#set xaxis range
plt.xlim(-10, 15)
# display label for line
plt.legend()
# display graph
plt.show()


