import numpy as np
from ripser import ripser
from persim import plot_diagrams
import matplotlib.pyplot as plt

import ellipse_tools

## parameters for ellipse
num_points = 100
a = np.sqrt(2)

## generate points on ellipse
interval = np.linspace(0, 1, num_points)
data = np.array(ellipse_tools.get_ellipse_points(interval, a))

## graph points on ellipse
plt.scatter(data[:,0], data[:,1])
plt.axis('equal')
plt.savefig('points_on_ellipse.png')

## compute persistence diagrams
plt.clf()
diagrams = ripser(data, maxdim=3)['dgms']
print(diagrams)
plot_diagrams(diagrams)
plt.savefig('ellipse_persistence_diagram.png')