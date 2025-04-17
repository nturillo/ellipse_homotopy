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
    interval_stretched = [i * ellipse_circumference for i in interval]
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

# C functions
libcomp = ctypes.CDLL('./libcomp.so')

libcomp.find_d_distance_point_on_ellipse.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
libcomp.find_d_distance_point_on_ellipse.restype = ctypes.c_double

libcomp.find_d_distance_point_on_ellipse_2.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
libcomp.find_d_distance_point_on_ellipse_2.restype = ctypes.c_double

libcomp.num_loops.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
libcomp.num_loops.restype = ctypes.c_int

libcomp.num_loops_2.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
libcomp.num_loops_2.restype = ctypes.c_int

def find_d_distance_point_on_ellipse(d, x, y, a):
    arr = (ctypes.c_double * 2)()
    libcomp.find_d_distance_point_on_ellipse(d, x, y, a, arr)
    return arr[0], arr[1]

def find_d_distance_point_on_ellipse_2(d, t, a):
    res_t = ctypes.c_double()
    libcomp.find_d_distance_point_on_ellipse_2(d, t, a, res_t)
    return res_t.value

def num_loops(d, x_0, y_0, a, num_steps):
    return libcomp.num_loops(d, x_0, y_0, a, num_steps)

def num_loops_2(d, t, a, num_steps):
    return libcomp.num_loops_2(d, t, a, num_steps)

libcomp.min_r_given_theta.argtypes = [ctypes.c_double, ctypes.c_double]
libcomp.min_r_given_theta.restype = ctypes.c_double

libcomp.min_r_given_theta_2.argtypes = [ctypes.c_double, ctypes.c_double]
libcomp.min_r_given_theta_2.restype = ctypes.c_double

def min_r_given_theta(theta, a):
    return libcomp.min_r_given_theta(theta, a)

def min_r_given_theta_2(theta, a):
    return libcomp.min_r_given_theta_2(theta, a)

 
def plot_k_points_d_Euclid_apart(k, d, theta, a, img_name = "points_on_ellipse.png", plot_foci=True, verbose = True, titled=False):
    ## plot k many points starting at (a*cos(t), sin(t)) and going around counter-clockwise, each a Euclidean distance d apart
    ## k = number of points
    ## d = Euclidean distance apart
    ## theta = angle of starting point
    ## a = semi-major axis

    x_0, y_0 = (a*np.cos(theta), np.sin(theta))

    num_steps = k
    if verbose:
        loops = num_loops(d, x_0, y_0, a, num_steps)
        print(f'num_loops = {loops}')

    points = [(x_0, y_0)]
    for i in range(num_steps):
        (x, y) = find_d_distance_point_on_ellipse(d, points[i][0], points[i][1], a)
        points.append((x, y))

    ## fix the axis limits
    fig, ax = plt.subplots()
    ax.set_xlim(-np.sqrt(2) - 0.1, np.sqrt(2) + 0.1)
    ax.set_ylim(-1.1, 1.1)

    ## plot the ellipse as a thin black line
    t = np.linspace(0, 2*np.pi, 100)
    ax.plot(a*np.cos(t), np.sin(t), 'k')

    ## foci
    if (plot_foci):
        c = np.sqrt(a**2 - 1)
        ax.scatter([-c, c], [0, 0], color='red')

    ## plot the points on the ellipse labelled by the step
    points = np.array(points)
    ax.scatter(points[:,0], points[:,1])
    for i, txt in enumerate(range(num_steps)):
        plt.annotate(txt, (points[i,0], points[i,1]))
    #ax.axis('equal')

    ## draw lines between points
    ax.plot(points[:,0], points[:,1])

    ## add title
    if titled:
        ax.set_title(f'k = {k}, d = {d}, theta = {theta}, a = {a}')

    ## save plot
    plt.savefig(img_name)
    plt.close()

    ## print points
    if verbose:
        for i, point in enumerate(points):
            print(f'point {i}: {point}')