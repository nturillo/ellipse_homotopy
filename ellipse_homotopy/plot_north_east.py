import ellipse_tools
import numpy as np

a_vals = np.linspace(1.0, 1.05, 1000)[1:]

k = 5
loops = 2

east_rs = [ellipse_tools.min_r_given_theta(theta=0, a=a_val, num_steps=k, num_loops=loops) for a_val in a_vals]
north_rs = [ellipse_tools.min_r_given_theta(theta=np.pi/2, a=a_val, num_steps=k, num_loops=loops) for a_val in a_vals]
difference = np.array(north_rs) - np.array(east_rs)

import matplotlib.pyplot as plt
plt.plot(a_vals, difference, label=r'min$_r$(North) - min$_r$(East)')

## plot 0 values in red
zeros = np.where(abs(difference) < 0.00000001)[0]
plt.scatter(a_vals[zeros], difference[zeros], color='red')

#plt.title('Difference between minimal edge length of triangle at North and East poles')

plt.xlabel('a')
plt.ylabel(r'Difference')
plt.legend()
plt.savefig(f'images/north_vs_east/north_east_diff_{k}.png')
