## functions for generating evenly spaced points on ellipse
## https://www.johndcook.com/blog/2022/11/02/ellipse-rng/
from scipy.special import ellipe, ellipeinc
from numpy import pi, sin, cos
from scipy.optimize import newton

def E_inverse(z, m):
    em = ellipe(m)
    t = (z/em)*(pi/2)
    f = lambda y: ellipeinc(y, m) - z
    r = newton(f, t)
    return r

def t_from_length(length, a, b):
    m = 1 - (b/a)**2
    T = 0.5*pi - E_inverse(ellipe(m) - length/a, m)
    return T

def get_ellipse_points(interval, a, b = 1):
    eccentricity_sq = 1.0 - (b/a)**2
    ellipse_circumference = 4 * a * ellipe(eccentricity_sq)
    interval_stretched = interval * ellipse_circumference
    Ts = [t_from_length(i, a, b) for i in interval_stretched]
    return [(a*cos(t), b*sin(t)) for t in Ts]

def get_ellipse_points_ts(interval, a, b = 1):
    eccentricity_sq = 1.0 - (b/a)**2
    ellipse_circumference = 4 * a * ellipe(eccentricity_sq)
    interval_stretched = interval * ellipse_circumference
    Ts = [t_from_length(i, a, b) for i in interval_stretched]
    return Ts

def plot_ellipse_points(interval, a, b = 1, img_name = "points_on_ellipse.png"):
    points = get_ellipse_points(interval, a, b)
    points = np.array(points)
    t = np.linspace(0, 2*np.pi, 100)
    plt.plot(a*np.cos(t), b*np.sin(t), 'k')
    plt.scatter(points[:,0], points[:,1])
    plt.axis('equal')
    plt.savefig(img_name)

## functions for computing points on ellipse d Euclidean distance apart
import ctypes
import matplotlib.pyplot as plt
import numpy as np

def plot_k_points_d_Euclid_apart(k, d, x_0, y_0, a, img_name = "points_on_ellipse.png"):
    libcomp = ctypes.CDLL('./libcomp.so')

    libcomp.find_d_distance_point_on_ellipse.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
    libcomp.find_d_distance_point_on_ellipse.restype = None

    libcomp.num_loops.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
    libcomp.num_loops.restype = ctypes.c_int

    def find_d_distance_point_on_ellipse(d, x, y, a):
        arr = (ctypes.c_double * 2)()
        libcomp.find_d_distance_point_on_ellipse(d, x, y, a, arr)
        return arr[0], arr[1]

    def num_loops(d, x_0, y_0, a, num_steps):
        return libcomp.num_loops(d, x_0, y_0, a, num_steps)

    num_steps = k
    num_loops = num_loops(d, x_0, y_0, a, num_steps)
    print(f'num_loops = {num_loops}')

    points = [(x_0, y_0)]
    for i in range(num_steps):
        x, y = find_d_distance_point_on_ellipse(d, points[i][0], points[i][1], a)
        points.append((x, y))

    ## plot the ellipse as a thin black line
    t = np.linspace(0, 2*np.pi, 100)
    plt.plot(a*np.cos(t), np.sin(t), 'k')

    ## plot the points on the ellipse labelled by the step
    points = np.array(points)
    plt.scatter(points[:,0], points[:,1])
    for i, txt in enumerate(range(num_steps + 1)):
        plt.annotate(txt, (points[i,0], points[i,1]))
    plt.axis('equal')

    ## save plot
    plt.savefig(img_name)

    ## print points
    for i, point in enumerate(points):
        print(f'point {i}: {point}')