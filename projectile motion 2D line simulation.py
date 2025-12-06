# import library
import matplotlib.pyplot as plt
import numpy as np

#function that shows specific frame of projectile
def spframe():
    t_deg = float(input("Enter theta (degrees): "))
    g = float(input("Enter acceleration due to gravity: "))
    u = float(input("Enter initial velocity: "))

    t = np.radians(t_deg)

    hight = (u ** 2 * np.sin(t) ** 2) / (2 * g)
    range = (u ** 2 * np.sin(2 * t)) / g
    proj = (range/2) * np.tan(t) - ((g * (range/2) ** 2) / (2 * u ** 2 * np.cos(t) ** 2))

    x = np.linspace(0, range, 100)
    y = np.linspace(0, hight, 100)
    xm, ym = np.meshgrid(x, y)
    zm = (xm - ym) * 0


    zf = []
    r = np.linspace(0, range, 100)
    for kz in r:
        zi = kz * np.tan(t) - ((g * kz ** 2) / (2 * u ** 2 * np.cos(t) ** 2))
        if zi >= 0:
            zf.append(zi)
        else:
            break

    print("zf:", zf)
    pr=[]
    xr=[]
    for i,j  in zip(zf,x):

        pr.append(i)
        xr.append(j)

        plt.xlim(0, range + 5)
        plt.ylim(0, hight + 5)

        plt.plot(xr, pr, c='r')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.pause(0.001)
        plt.cla()

    plt.show()

    print("Range: ", range)
    print("Height: ", hight)


#function that shows general frame of projectile
def gframe():
    t_deg = float(input("Enter theta (degrees): "))
    g = float(input("Enter acceleration due to gravity: "))
    u = float(input("Enter initial velocity: "))

    t = np.radians(t_deg)

    hight = (u ** 2 * np.sin(t) ** 2) / (2 * g)
    range = (u ** 2 * np.sin(2 * t)) / g
    proj = (range/2) * np.tan(t) - ((g * (range/2) ** 2) / (2 * u ** 2 * np.cos(t) ** 2))

    x = np.linspace(0, range, 100)
    y = np.linspace(0, hight, 100)
    xm, ym = np.meshgrid(x, y)
    zm = (xm - ym) * 0


    zf = []
    r = np.linspace(0, range, 100)
    for kz in r:
        zi = kz * np.tan(t) - ((g * kz ** 2) / (2 * u ** 2 * np.cos(t) ** 2))
        if zi >= 0:
            zf.append(zi)
        else:
            break

    print("zf:", zf)
    pr=[]
    xr=[]
    for i,j  in zip(zf,x):

        pr.append(i)
        xr.append(j)

        plt.xlim(0, max(range,hight)+5)
        plt.ylim(0, max(range,hight)+5)

        plt.plot(xr, pr, c='r')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.pause(0.001)
        plt.cla()

    plt.show()

    print("Range: ", range)
    print("Height: ", hight)



spframe()
gframe()