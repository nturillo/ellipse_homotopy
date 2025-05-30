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

libcomp.max_loops.argtypes = [ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.c_int, ctypes.c_int]
libcomp.max_loops.restype = ctypes.c_int

def max_loops(d, points, a, num_steps, stop_early = 0):
    num_points = len(points)
    x_arr = (ctypes.c_double * num_points)()
    y_arr = (ctypes.c_double * num_points)()
    for i, point in enumerate(points):
        x_arr[i] = point[0]
        y_arr[i] = point[1]
    max_arr = (ctypes.c_double * 2)()
    max_loops = libcomp.max_loops(d, num_points, x_arr, y_arr, max_arr, a, num_steps, stop_early)
    return max_loops, max_arr[0], max_arr[1]

## for a \in [1, sqrt(2)], determine the least d such that there is some point on the ellipse which makes 2 loops after 5 steps of d-distance apart points
num_ellipses = 10000
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
        max, x_max, y_max = max_loops(d, points, a_val, num_steps, stop_early = 2)
        if max < num_loops:
            left = d
        else:
            right = d
    d_vals.append(d)
    max_points.append((x_max, y_max))

## plot d vs a
plt.clf()
plt.figure(dpi=300)
plt.plot(a_vals, d_vals)
plt.xlabel('a')
plt.ylabel('r')
plt.title('smallest r such that k_5 appears in r-distance\n Vietoris-Rips complex of ellipse with semi-major axis a')
plt.savefig('r_vs_a.png')

## plot points on the ellipse that maximize the number of loops after 5 steps of d-distance apart points
plt.clf()
plt.figure(dpi=300)

# plot a couple ellipses for reference
t = np.linspace(0, np.pi/2, 100)
for a_val in a_vals[::2000]:
    plt.plot(a_val * np.cos(t), np.sin(t))
plt.plot(a_vals[-1] * np.cos(t), np.sin(t))

for i, points in enumerate(max_points):
    plt.scatter(points[0], points[1])
    # color the points by the value of from red to blue
    plt.scatter(points[0], points[1], color = [i / num_ellipses, 0, 1 - i / num_ellipses])
    # annotate every tenth point
    if i % 1000 == 0 or i == 79 or i == 99:
        plt.annotate(f'{i}', (points[0], points[1]), fontsize=6)

## draw a rectangle around the first 79 points
def bounding_rectangle(points, margin=0):
    points = np.array(points)  # Convert to NumPy array
    min_x, min_y = np.min(points, axis=0)
    max_x, max_y = np.max(points, axis=0)

    return (min_x - margin, min_y - margin, max_x + margin, max_y + margin)

min_x, min_y, max_x, max_y = bounding_rectangle(max_points[:79], margin=0.04)
rect = plt.Rectangle((min_x, min_y), max_x-min_x, max_y-min_y, edgecolor='black', facecolor='none', linewidth=1, label="Bounding Box")
plt.gca().add_patch(rect)

# Add a caption to the left of the rectangle
caption = "Points 0-78"
plt.gca().text(min_x - 0.03, min_y, caption, va='center', ha='right', fontsize=12)


plt.axis('equal')
plt.savefig('points_max_loops.png')

    