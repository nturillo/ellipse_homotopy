import numpy as np
import ellipse_tools

a_vals = np.linspace(1.0, np.sqrt(2), 1000)

theta = 0

r_vals = [ellipse_tools.min_r_given_theta(theta, a) for a in a_vals]
pt1s = [ellipse_tools.find_d_distance_point_on_ellipse(r, a, 0, a) for a, r in zip(a_vals, r_vals)]
pt2s = [ellipse_tools.find_d_distance_point_on_ellipse(r, pt1[0], pt1[1], a) for pt1, r, a in zip(pt1s, r_vals, a_vals)]

ratios = [pt1[1] / pt1[0] for pt1 in pt1s]

## plot ratios vs a vals
import matplotlib.pyplot as plt
plt.plot(a_vals, ratios)
plt.xlabel('a')
plt.ylabel('ratio')
plt.title('ratio of y/x vs a')
plt.grid()
plt.savefig('ratios_vs_a.png')