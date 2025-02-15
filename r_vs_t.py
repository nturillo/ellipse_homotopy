import numpy as np
import ctypes
import matplotlib.pyplot as plt

import ellipse_tools

libcomp = ctypes.CDLL('./libcomp.so')

libcomp.min_r_given_t.argtypes = [ctypes.c_double, ctypes.c_double]
libcomp.min_r_given_t.restype = ctypes.c_double

def min_r_given_t(t, a):
    return libcomp.min_r_given_t(t, a)

## parameters
a = np.linspace(1.329, 1.331, 20)
num_points = 1000

for a_val in a:
    ## get evenly spaced points 
    interval = np.linspace(0, 1/4, num_points)
    Ts = ellipse_tools.get_ellipse_points_ts(interval, a_val)
    Rs = [min_r_given_t(t, a_val) for t in Ts]

    ## plot
    plt.clf()
    plt.plot(Ts, Rs)
    plt.xlabel('t')
    plt.ylabel('r')
    plt.title('r vs t')
    plt.savefig(f'r_vs_t/r_vs_t_a={a_val}.png')

