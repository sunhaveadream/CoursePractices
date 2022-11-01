#try15-3
#2022/11/2
#author:linxu

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # rw = RandomWalk()
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('classic')
    # fig,ax=plt.subplots()
    fig, ax = plt.subplots(figsize=(19,9))
    # print(len(rw.x_values))
    # print(len(rw.y_values))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values,rw.y_values,linewidth=1)

    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("是否进行下一场随机漫步？ y/n:")
    if keep_running == 'n':
        break