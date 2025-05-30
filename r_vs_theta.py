import numpy as np
import ctypes
import matplotlib.pyplot as plt
import csv


import ellipse_tools

libcomp = ctypes.CDLL('./libcomp.so')

def find_local_minima(values):
    return [i for i in range(1, len(values) - 1) if values[i] < values[i - 1] and values[i] < values[i + 1]]

def find_local_maxima(values):
    return [i for i in range(1, len(values) - 1) if values[i] > values[i - 1] and values[i] > values[i + 1]]


## parameters
# 1.412273647850328
# 1.3299220317449445
a = [1.3299220317449445+0.005] #np.linspace(1.329, 1.331, 40)
num_points = 20000
plot_minima_and_maxima = True 

for i, a_val in enumerate(a):
    ## get evenly spaced points 
    interval = np.linspace(0.0, 0.25, num_points)
    thetas = ellipse_tools.get_ellipse_points_ts(interval, a_val)
    Rs = [ellipse_tools.min_r_given_theta(theta, a_val) for theta in thetas]

    ## plot
    plt.clf()
    plt.plot(thetas, Rs)
    plt.xlabel('t')
    plt.ylabel('r')
    plt.title('r vs t')
    plt.savefig(f'r_vs_t/{i}_r_vs_theta_a={a_val}.png')

    if plot_minima_and_maxima:
        minima_is = find_local_minima(Rs)
        maxima_is = find_local_maxima(Rs)

        image_dir = "images"

        for i in minima_is:
            print(f"minima: {i}, theta: {thetas[i]}, r: {Rs[i]}")
            ellipse_tools.plot_k_points_d_Euclid_apart(k=5, d=Rs[i], theta=thetas[i], a=a_val, img_name=f"{image_dir}/minima_{i}_a={a_val}.png", verbose=True, titled=True)
        for i in maxima_is:
            print(f"maxima: {i}, theta: {thetas[i]}, r: {Rs[i]}")
            ellipse_tools.plot_k_points_d_Euclid_apart(k=5, d=Rs[i], theta=thetas[i], a=a_val, img_name=f"{image_dir}/maxima_{i}_a={a_val}.png", verbose=True, titled=True)

        with open(f"csv/output_{a[0]=:.5f}", mode = 'w', newline= '') as file:
            writer = csv.writer(file)
            writer.writerow(['min/max', 'num', 'theta','R'])
            for i in minima_is:
                writer.writerow(['min', i, thetas[i],Rs[i]])
            for i in maxima_is:
                writer.writerow(['max', i, thetas[i],Rs[i]])
    