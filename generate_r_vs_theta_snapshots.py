import numpy as np
import ellipse_tools

# This code finds a-values in the range (1, sqrt(2)] where the extrema of r_vs_t change, and takes snapshots 
############################################################################################################


# first, find switches
a_list = np.linspace(1.03, np.sqrt(2), num=1000, endpoint=True)[1:]
north_r_list = [ellipse_tools.min_r_given_theta(theta=np.pi/2, a=a) for a in a_list]
east_r_list = [ellipse_tools.min_r_given_theta(theta=0, a=a) for a in a_list]
a_pairs = []
for i in range(len(a_list)-1):
    if (north_r_list[i] > east_r_list[i]) != (north_r_list[i+1] > east_r_list[i+1]):
        a_pairs.append((a_list[i], a_list[i+1]))

# find points where north_r = east_r
equal_a_list = []
for (min_a, max_a) in a_pairs:
    min_north_bigger = ellipse_tools.min_r_given_theta(theta=np.pi/2, a=min_a) > ellipse_tools.min_r_given_theta(theta=0, a=min_a)
    while max_a - min_a > 1e-15:
        a = (min_a + max_a) / 2
        north_r = ellipse_tools.min_r_given_theta(theta=np.pi/2, a=a)
        east_r = ellipse_tools.min_r_given_theta(theta=0, a=a)
        if min_north_bigger:
            if north_r > east_r:
                min_a = a
            else:
                max_a = a
        else:
            if north_r > east_r:
                max_a = a
            else:
                min_a = a
    equal_a_list.append(a)

print(f"Equal a list: {equal_a_list}")

ellipse_tools.plot_r_vs_theta(a = 1.2, img_path=f"Snapshots/0_a={1.2:.3f}.png")
img_idx = 1
range = 0.0001
for i, a in enumerate(equal_a_list):
    ellipse_tools.plot_r_vs_theta(a = a-range, img_path=f"Snapshots/{img_idx}_a={a-range:.4f}.png")
    ellipse_tools.plot_r_vs_theta(a = a, img_path=f"Snapshots/{img_idx+1}_a={a:.4f}.png")
    ellipse_tools.plot_r_vs_theta(a = a+range, img_path=f"Snapshots/{img_idx+2}_a={a+range:.4f}.png")
    img_idx += 3

    if i != len(equal_a_list)-1:
        mid_a = (a + equal_a_list[i+1]) / 2
        ellipse_tools.plot_r_vs_theta(a = mid_a, img_path=f"Snapshots/{img_idx+1}_a={mid_a:.4f}.png")
        img_idx += 1

ellipse_tools.plot_r_vs_theta(a = np.sqrt(2), img_path=f"Snapshots/{img_idx}_a={a:.3f}.png")
