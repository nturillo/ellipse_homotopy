import numpy as np
import ellipse_tools
import matplotlib.pyplot as plt

a_vals = np.linspace(1.0, np.sqrt(2), 1000)

theta = 0

for a in a_vals[::100]:
    r = ellipse_tools.min_r_given_theta(theta, a)
    pt0 = (a * np.cos(theta), np.sin(theta))
    pt1 = ellipse_tools.find_d_distance_point_on_ellipse(r, pt0[0], pt0[1], a)
    pt2 = ellipse_tools.find_d_distance_point_on_ellipse(r, pt1[0], pt1[1], a)

    ## plot pt0, pt1, pt2 for a few a vals
    fig, ax = plt.subplots()
    ax.set_xlim(-a, a)
    ax.set_ylim(-a, a)
    ## plot ellipse
    thetas = np.linspace(0, 2 * np.pi, 1000)
    xs = a * np.cos(thetas)
    ys = np.sin(thetas)
    ax.plot(xs, ys)
    ## plot pt0, pt1, pt2 with labels
    ax.plot(pt0[0], pt0[1], 'ro', label='pt0')
    ax.plot(pt1[0], pt1[1], 'go', label='pt1')
    ax.plot(pt2[0], pt2[1], 'bo', label='pt2')

    plt.savefig(f'ellipse_{a:.3f}.png')
