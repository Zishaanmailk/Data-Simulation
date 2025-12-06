import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.DataFrame()
x=np.linspace(-4*(22/7),4*(22/7),9999)

try:
    phase = int(input("Enter number of phase: "))
    div = (2 * np.pi) / phase
    deg = 360 / phase
    divl = np.arange(0, 2 * np.pi+div, div)  # phase offsets in radians
    degl = np.arange(0, 360+ deg, deg)        # phase offsets in degrees
except Exception:
    print("please enter only integer")
    exit(1)

for i,j in zip(range(phase),divl):
    data[i]=np.sin(j+x) # phase shifted sine waves

def plot(data):
    fig, ax = plt.subplots(3, 1)
    fig.suptitle('AC phase simulation', fontsize=16)

    #ploting single phase
    sns.lineplot(x=x, y=np.sin(x), label="y=sin(x)", ax=ax[0])
    ax[0].axhline(0, color='gray', linestyle='--')

    #ploting multi phase
    for k, l in zip(range(phase), degl):
        sns.lineplot(x=x, y=data[k], label=f"y=sin({l}° + x)", ax=ax[1])
    ax[1].axhline(0, color='gray', linestyle='--')

    data['final'] = data.sum(axis=1)
    print(data)
    #ploting summation of multi phase
    sns.lineplot(x=x, y=data['final'], label="Sum of all phases", ax=ax[2])
    ax[2].axhline(0, color='gray', linestyle='--')
    ax[2].set_ylim(-1.2,1.2)

    txl = ['-4π', '-3π', '-2π', '-1π', '0', '1π', '2π', '3π', '4π']
    tx = np.arange(-4 * np.pi, 4.1 * np.pi, np.pi)
    ax[2].set_xticks(tx)
    ax[2].set_xticklabels(txl)
    plt.tight_layout()
    plt.show()

plot(data)