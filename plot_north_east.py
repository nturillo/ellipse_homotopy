import ellipse_tools
import numpy as np

a_vals = np.linspace(1.0, np.sqrt(2), 1000)

east_rs = [ellipse_tools.min_r_given_theta(theta=0, a=a_val) for a_val in a_vals]
north_rs = [ellipse_tools.min_r_given_theta(theta=np.pi/2, a=a_val) for a_val in a_vals]
difference = np.array(north_rs) - np.array(east_rs)

import matplotlib.pyplot as plt
plt.plot(a_vals, difference, label='min_r(North_Pole) - min_r(East_Pole)')
plt.xlabel('a')
plt.ylabel('r')
plt.legend()
plt.savefig('north_vs_east.png')
