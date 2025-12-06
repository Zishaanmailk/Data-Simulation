import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.animation import FuncAnimation

#Setup
data = pd.DataFrame()
x = np.linspace(-4 * (22 / 7), 4 * (22 / 7), 9999)

#Input phase
try:
    phase = int(input("Enter number of phase: "))
    div = (2 * np.pi) / phase
    deg = 360 / phase
    divl = np.arange(0, 2 * np.pi + div, div)[:phase]  # ensure exact 'phase' values
    degl = np.arange(0, 360 + deg, deg)[:phase]
except Exception:
    print("Please enter only an integer")
    exit(1)

#Generate phase shifted sine waves
for i, j in zip(range(phase), divl):
    data[i] = np.sin(j + x)

data['final'] = data.sum(axis=1)

#Plot function with animation
def plot(data):
    sns.set(style="darkgrid")
    fig, ax = plt.subplots(3, 1, figsize=(12, 10))
    fig.suptitle('AC phase simulation (Animated)', fontsize=16)

    #Single phase sine
    line1, = ax[0].plot([], [], label="y=sin(x)")
    ax[0].axhline(0, color='gray', linestyle='--')
    ax[0].legend()
    ax[0].set_xlim(x[0], x[-1])
    ax[0].set_ylim(-1.2, 1.2)

    #Multi-phase sine
    lines2 = []
    for k in range(phase):
        ln, = ax[1].plot([], [], label=f"y=sin({int(degl[k])}° + x)")
        lines2.append(ln)
    ax[1].axhline(0, color='gray', linestyle='--')
    #ax[1].legend()
    ax[1].set_xlim(x[0], x[-1])
    ax[1].set_ylim(-1.2, 1.2)

    # 3. Sum of phases
    line3, = ax[2].plot([], [], label="Sum of all phases")
    ax[2].axhline(0, color='gray', linestyle='--')
    ax[2].set_ylim(-1.2 * phase, 1.2 * phase)
    ax[2].set_xlim(x[0], x[-1])
    ax[2].legend()

    #π ticks
    txl = ['-4π', '-3π', '-2π', '-π', '0', 'π', '2π', '3π', '4π']
    tx = np.arange(-4 * np.pi, 4.1 * np.pi, np.pi)
    ax[2].set_xticks(tx)
    ax[2].set_xticklabels(txl)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    #Animation function
    def animate(i):
        #Update single phase
        line1.set_data(x[:i], np.sin(x[:i]))

        #Update all phase-shifted
        for k, line in enumerate(lines2):
            line.set_data(x[:i], data[k][:i])

        #Update sum of all pahse
        line3.set_data(x[:i], data['final'][:i])

    ani = FuncAnimation(fig, animate, frames=range(0,len(x)+5,50), interval=5, repeat=False)
    plt.show()

plot(data)
