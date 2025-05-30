import ellipse_tools
import numpy as np

a = 1.2
k = 5
theta = np.pi/2

#t_ellipse = ellipse_tools.get_ellipse_points_ts(np.array([t]), a)[0]
d = ellipse_tools.min_r_given_theta(theta, a, num_steps=3, num_loops=1)
print(f"theta = {theta}, d = {d}")
ellipse_tools.plot_k_points_d_Euclid_apart(k, d, theta, a, f"a={a}_triangle.png", verbose = True)
