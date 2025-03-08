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
num_points = 1000
a = np.linspace(1.0, np.sqrt(2), num_points)
interval = np.linspace(0, 0.25, num_points)
rs = []

for a_val in a:
    ## get evenly spaced points 
    ts = ellipse_tools.get_ellipse_points_ts(interval, a_val)
    rs_by_a = [min_r_given_t(t, a_val) for t in ts]
    rs.append(rs_by_a)


rs = np.array(rs)
np.save('r_vs_t_surface.npy', rs)

## create .obj file
with open('r_vs_a_vs_t_surface.obj', 'w') as f:
    for i in range(num_points):
        for j in range(num_points):
            f.write(f'v {a[i]} {interval[j]} {rs[i][j]}\n')

    for i in range(num_points - 1):
        for j in range(num_points - 1):
            f.write(f'f {i*num_points + j + 1} {i*num_points + j + 2} {(i+1)*num_points + j + 2}\n')
            f.write(f'f {i*num_points + j + 1} {(i+1)*num_points + j + 2} {(i+1)*num_points + j + 1}\n')
