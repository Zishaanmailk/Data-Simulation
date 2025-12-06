# import library
import matplotlib.pyplot as plt
import numpy as np

#function that shows specific frame of projectile with zaxis
def yesz():
    ax = plt.axes(projection="3d")

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

    for i, zi in zip(r, zf):


        ax.set_xlim(0, range + 5)
        ax.set_ylim(0, hight + 5)
        ax.set_zlim(0, proj + 5)

        ax.plot_surface(xm, ym, zm, alpha=0.3)
        ax.scatter(i, zi, zi, c='r')
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        plt.pause(0.001)
        plt.cla()

    plt.show()

    print("Range: ", range)
    print("Height: ", hight)


#function that shows general frame of projectile with zaxis
def gyesz():
    ax = plt.axes(projection="3d")

    t_deg = float(input("Enter theta (degrees): "))
    g = float(input("Enter acceleration due to gravity: "))
    u = float(input("Enter initial velocity: "))

    t = np.radians(t_deg)

    hight = (u ** 2 * np.sin(t) ** 2) / (2 * g)
    range = (u ** 2 * np.sin(2 * t)) / g
    proj = (range/2) * np.tan(t) - ((g * (range/2) ** 2) / (2 * u ** 2 * np.cos(t) ** 2))

    x = np.linspace(0, max(range,hight,proj), 100)
    y = np.linspace(0, max(range,hight,proj), 100)
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

    for i, zi in zip(r, zf):


        ax.set_xlim(0, max(range,hight,proj)+5)
        ax.set_ylim(0, max(range,hight,proj)+5)
        ax.set_zlim(0, max(range,hight,proj)+5)

        ax.plot_surface(xm, ym, zm, alpha=0.3)
        ax.scatter(i, zi, zi, c='r')
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        plt.pause(0.001)
        plt.cla()

    plt.show()

    print("Range: ", range)
    print("Height: ", hight)


#function that shows specific frame of projectile without zaxis
def noz():
    ax = plt.axes(projection="3d")

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

    for i, zi in zip(r, zf):


        ax.set_xlim(0, range + 5)
        ax.set_ylim(0, hight + 5)
        ax.set_zlim(0, proj + 5)

        ax.plot_surface(xm, ym, zm, alpha=0.3)
        ax.scatter(i, zi, 0, c='r')
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        plt.pause(0.001)
        plt.cla()

    plt.show()

    print("Range: ", range)
    print("Height: ", hight)



#function that shows general frame of projectile without zaxis
def gnoz():
    ax = plt.axes(projection="3d")

    t_deg = float(input("Enter theta (degrees): "))
    g = float(input("Enter acceleration due to gravity: "))
    u = float(input("Enter initial velocity: "))

    t = np.radians(t_deg)

    hight = (u ** 2 * np.sin(t) ** 2) / (2 * g)
    range = (u ** 2 * np.sin(2 * t)) / g
    proj = (range/2) * np.tan(t) - ((g * (range/2) ** 2) / (2 * u ** 2 * np.cos(t) ** 2))

    x = np.linspace(0, max(range,hight,proj), 100)
    y = np.linspace(0, max(range,hight,proj), 100)
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

    for i, zi in zip(r, zf):


        ax.set_xlim(0, max(range,hight,proj)+5)
        ax.set_ylim(0, max(range,hight,proj)+5)
        ax.set_zlim(0, max(range,hight,proj)+5)

        ax.plot_surface(xm, ym, zm, alpha=0.3)
        ax.scatter(i, zi, 0, c='r')
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        plt.pause(0.001)
        plt.cla()

    plt.show()

    print("Range: ", range)
    print("Height: ", hight)




yesz()
noz()
gyesz()
gnoz()