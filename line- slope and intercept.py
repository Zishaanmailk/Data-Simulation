# import library
import matplotlib.pyplot as plt
import numpy as np


# Function to plot a line given a random  slope and intercept
def plot_line1():

    # Generate random slope and intercept values
    slope = np.random.randint(-10, 10)
    intercept = np.random.randint(-20, 20)

    x = np.linspace(-10, 10, 100)  # Define x range
    y = slope * x + intercept                 # Line equation y = mx + c

    # Plotting
    plt.plot(x, y, label=f'Slope = {slope}, Intercept = {intercept}')
    plt.axhline(0, color='black',linewidth=0.5)  # X-axis
    plt.axvline(0, color='black',linewidth=0.5)  # Y-axis
    plt.title('Line with Given Slope and Intercept')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()


# Function to plot a line given a slope and intercept
def plot_line2(slope, intercept):

    x = np.linspace(-10, 10, 1000)  # Define x range
    y = slope * x + intercept                # Line equation y = mx + c

    # Plotting
    plt.plot(x, y, label=f'Slope = {slope}, Intercept = {intercept}')
    plt.axhline(0, color='black', linewidth=0.5)  # X-axis
    plt.axvline(0, color='black', linewidth=0.5)  # Y-axis
    plt.title('Line with Given Slope and Intercept')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()


# calling functions1
plot_line1()

#input parameters
slope=float(input("Enter slope :  "))
intercept=float(input("Enter intercept :  "))

# calling functions1
plot_line2(slope, intercept)
print(slope)
print(intercept)