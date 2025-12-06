# import library
import numpy as np
import matplotlib.pyplot as plt

#generate x ,y points
x=np.linspace(-4*(22/7),4*(22/7),9999)
y=np.cos(x)

#ploting
txl=['-4pi','-3pi','-2pi','-1pi','0pi','1pi','2pi','3pi','4pi'] #xticks-label
tx=list(np.arange(-4*np.pi,4.1*np.pi, np.pi))                   #xticks
plt.plot(x, y, label="y=cos(x)")                          #line plot
plt.title("cos wave")
plt.xlabel("x")
plt.ylabel("y")
plt.xticks(tx,txl)
# make mid-value of x number line as 0
plt.axhline(0)
#make mid-value of x number line as 0
plt.axvline(0)
#display label for line
plt.legend()
# display graph
plt.show()


