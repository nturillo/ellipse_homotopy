import numpy as np
from ripser import ripser
from persim import plot_diagrams
import matplotlib.pyplot as plt

## parameters for ellipse
num_points = 100
a = np.sqrt(2)
b = 1

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

def get_even_ellipse_points(num_points, a, b = 1):
    eccentricity_sq = 1.0 - (b/a)**2
    ellipse_circumference = 4 * a * ellipe(eccentricity_sq)
    interval = np.linspace(0, ellipse_circumference, num_points)
    Ts = [t_from_length(i, a, b) for i in interval]
    return [(a*cos(t), b*sin(t)) for t in Ts]

## generate points on ellipse
data = np.array(get_even_ellipse_points(num_points, a, b))

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