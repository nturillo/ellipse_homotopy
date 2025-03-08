import numpy as np
import ctypes
import matplotlib.pyplot as plt

import ellipse_tools

libcomp = ctypes.CDLL('./libcomp.so')



## parameters
a = [1.0, 1.1, 1.2] # np.linspace(1.329, 1.331, 40)
num_points = 1000

for a_val in a:
    ## get evenly spaced points 
    interval = np.linspace(0.0, 0.25, num_points)
    Ts = ellipse_tools.get_ellipse_points_ts(interval, a_val)
    Rs = [ellipse_tools.min_r_given_t(t, a_val) for t in Ts]

    ## plot
    plt.clf()
    plt.plot(Ts, Rs)
    plt.xlabel('t')
    plt.ylabel('r')
    plt.title('r vs t')
    plt.savefig(f'r_vs_t/{a_val}_r_vs_t_a={a_val}.png')

