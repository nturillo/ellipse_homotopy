import numpy as np
import ctypes
import matplotlib.pyplot as plt

import ellipse_tools

libcomp = ctypes.CDLL('./libcomp.so')

libcomp.find_d_distance_point_on_ellipse.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
libcomp.find_d_distance_point_on_ellipse.restype = None

def find_d_distance_point_on_ellipse(d, x, y, a):
    arr = (ctypes.c_double * 2)()
    libcomp.find_d_distance_point_on_ellipse(d, x, y, a, arr)
    return arr[0], arr[1]

libcomp.num_loops.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
libcomp.num_loops.restype = ctypes.c_int

def num_loops(d, x_0, y_0, a, num_steps):
    return libcomp.num_loops(d, x_0, y_0, a, num_steps)

libcomp.max_loops.argtypes = [ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.c_int]
libcomp.max_loops.restype = ctypes.c_int

def max_loops(d, points, a, num_steps):
    num_points = len(points)
    x_arr = (ctypes.c_double * num_points)()
    y_arr = (ctypes.c_double * num_points)()
    for i, point in enumerate(points):
        x_arr[i] = point[0]
        y_arr[i] = point[1]
    max_arr = (ctypes.c_double * 2)()
    max_loops = libcomp.max_loops(d, num_points, x_arr, y_arr, max_arr, a, num_steps)
    return max_loops, max_arr[0], max_arr[1]

## for a \in [1, sqrt(2)], determine the least d such that there is some point on the ellipse which makes 2 loops after 5 steps of d-distance apart points
num_ellipses = 100
num_samples = 100
num_steps = 5
num_loops = 2
interval = np.linspace(0, 0.25, num_samples) # only sample points in first quadrant since these are the only points modulo symmetry

a_vals = np.linspace(1, np.sqrt(2), num_ellipses)
d_vals = []
max_points = []

for a_val in a_vals:
    # get ellipse points
    points = ellipse_tools.get_ellipse_points(interval, a_val)
    # binary search on d
    left = 0
    right = 2 * a_val
    max = 0
    while right - left > 1e-8 or max < num_loops:
        d = (left + right) / 2
        max, x_max, y_max = max_loops(d, points, a_val, num_steps)
        if max < num_loops:
            left = d
        else:
            right = d
    d_vals.append(d)
    max_points.append((x_max, y_max))

## plot d vs a
plt.clf()
plt.plot(a_vals, d_vals)
plt.xlabel('a')
plt.ylabel('r')
plt.title('smallest r such that k_5 appears in r-distance\n Vietoris-Rips complex of ellipse with semi-major axis a')
plt.savefig('r_vs_a.png')

    