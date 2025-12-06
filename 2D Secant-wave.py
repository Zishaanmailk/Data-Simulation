# import library
import numpy as np
import matplotlib.pyplot as plt

#generate x ,y points
x=np.linspace(-4*(22/7),4*(22/7),99999)
y = 1 / np.cos(x)
y[np.abs(np.cos(x)) < 1e-5] = np.nan  # avoid division by zero

#ploting
txl=['-4pi','-3pi','-2pi','-1pi','0pi','1pi','2pi','3pi','4pi'] #xticks-label
tx=list(np.arange(-4*np.pi,4.1*np.pi, np.pi))                   #xticks
ty=list(np.arange(-5,5,1))                                      #yticks
plt.plot(x, y, label="y=secant(x)")                        #line plot
plt.title("secant wave")
plt.xlabel("x")
plt.ylabel("y")
plt.xticks(tx,txl)
plt.yticks(ty)
#make mid-value of x number line as 0
plt.axhline(0)
#make mid-value of y number line as 0
plt.axvline(0)
#set yaxis range
plt.ylim(-5, 5)
plt.tight_layout()
#display label for line
plt.legend()
#display graph
plt.show()




