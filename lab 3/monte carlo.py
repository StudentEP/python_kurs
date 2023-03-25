coc) 745 Bytes
import matplotlib.pyplot as plt
import math
import random


def approximate_pi():
    times = 5000

    counter = 0
    x_in=[]
    y_in=[]
    x_out=[]
    y_out=[]
    for _ in range(times):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        if math.sqrt(x**2+y**2)<=1:
            counter += 1
            x_in.append(x)
            y_in.append(y)
        else:
            x_out.append(x)
            y_out.append(y)

    fig, ax = plt.subplots()
    circle=plt.Circle((0,0),1,color="red",fill=False)
    ax.add_patch(circle)
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    plt.scatter([x_in],[y_in],s=1,color="green")
    plt.scatter([x_out], [y_out], s=1, color="blue")
    plt.show()
    return 4*(counter/times)