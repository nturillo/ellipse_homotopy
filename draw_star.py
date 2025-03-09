import ellipse_tools
import numpy as np

a = np.sqrt(2)
k = 5
t = 0.125

t_ellipse = ellipse_tools.get_ellipse_points_ts(np.array([t]), a)[0]
d = ellipse_tools.min_r_given_t(t_ellipse, a)
ellipse_tools.plot_k_points_d_Euclid_apart(k, d, t, a, f"star_points.png", verbose = True)
