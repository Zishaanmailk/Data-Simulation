# import library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#generate x ,y points
x=np.linspace(-4*(22/7),4*(22/7),9999)

data=pd.DataFrame()
n=int(input("Enter number of phase"))
div=(2*np.pi)/n
divl=np.arange(0,2*np.pi+div,div)

for i,j in zip(range(n),divl):
    data[i]=np.sin(j+x)
print(data)