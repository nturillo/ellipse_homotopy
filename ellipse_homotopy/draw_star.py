import ellipse_tools
import numpy as np

a = 1.35
k = 5
theta = np.pi/2

#t_ellipse = ellipse_tools.get_ellipse_points_ts(np.array([t]), a)[0]
d = ellipse_tools.min_r_given_theta(theta, a)
print(f"theta = {theta}, d = {d}")
ellipse_tools.plot_k_points_d_Euclid_apart(k, d, theta, a, f"north_star.png", verbose = True, plot_foci=False)
