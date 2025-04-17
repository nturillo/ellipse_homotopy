import numpy as np
import ellipse_tools

# This code finds the value of a such that the minimum radius at the North Pole is equal to the minimum radius at the East Pole.

min_a = 1.2
max_a = 1.4

while (max_a - min_a) > 1e-15:
    a = (min_a + max_a) / 2
    north_r = ellipse_tools.min_r_given_theta(theta=np.pi/2, a=a)
    east_r = ellipse_tools.min_r_given_theta(theta=0, a=a)
    if north_r > east_r:
        min_a = a
    else:
        max_a = a
print(f"a: {a}, min_r(North_Pole): {north_r}, min_r(East_Pole): {east_r}")