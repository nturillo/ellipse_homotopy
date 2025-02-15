import numpy as np
import ctypes
import matplotlib.pyplot as plt

import ellipse_tools

libcomp = ctypes.CDLL('./libcomp.so')

libcomp.find_d_distance_point_on_ellipse.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
libcomp.find_d_distance_point_on_ellipse.restype = ctypes.c_double

def find_d_distance_point_on_ellipse(d, x, y, a):
    arr = (ctypes.c_double * 2)()
    libcomp.find_d_distance_point_on_ellipse(d, x, y, a, arr)
    return arr[0], arr[1]

def d_distance_point_error(d, x, y, a):
    arr = (ctypes.c_double * 2)()
    return abs(d - libcomp.find_d_distance_point_on_ellipse(d, x, y, a, arr))

## get ellipse points
a = 1.3
interval = np.linspace(0, 1/4, 10000)
Ts = ellipse_tools.get_ellipse_points_ts(interval, a)
points = ellipse_tools.get_ellipse_points(interval, a)

## for each point, get d distance point
d = 1.98    
errors = [d_distance_point_error(d, point[0], point[1], a) for point in points]

## plot errors vs t
plt.clf()
plt.plot(Ts, errors)
plt.xlabel('t')
plt.ylabel('error')
plt.title('error vs t')
plt.savefig("error_vs_t.png")

print("max error: ", max(errors))
print("min error: ", min(errors))
print("mean error: ", np.mean(errors))
print("std error: ", np.std(errors))
print("median error: ", np.median(errors))