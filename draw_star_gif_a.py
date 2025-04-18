import ellipse_tools
import numpy as np

import tempfile
from PIL import Image
import glob

## draw the smallest star in the ellipse (x/a)^2 + (y)^2 = 1 as a varies

a_list = np.linspace(1.0, np.sqrt(2), 500)
k = 5
t_list_1 = np.linspace(0.0, 0.01, 100)
t_list_2 = np.linspace(0.24, 0.25, 100)
t_list = np.concatenate((t_list_1, t_list_2))
t_list = [0, 0.25]

with tempfile.TemporaryDirectory() as tmpdir:
    for i, a in enumerate(a_list):
        min_r = 2.0
        argmin_r = 0.0
        thetas = ellipse_tools.get_ellipse_points_ts(t_list, a)
        for theta in thetas:
            if theta < 0.0 or theta > np.pi/2:
                print(f"theta = {theta} out of bounds")
        rs = [ellipse_tools.min_r_given_theta(t, a) for t in thetas]
        for i2, r in enumerate(rs):
            if r < min_r:
                min_r = r
                argmin_r = i2
        theta = thetas[argmin_r]
        ellipse_tools.plot_k_points_d_Euclid_apart(k, min_r, theta, a, f"{tmpdir}/{i}.png", verbose = False)
   
    image_files = sorted(glob.glob(f"{tmpdir}/*.png"), key=lambda x: int(x.split('/')[-1].split('.')[0]))

    images = [Image.open(image_file) for image_file in image_files]
    ## boomerang effect
    images = images + images[-2:0:-1]
    images[0].save(f'gifs/star_a={a_list[0]}-{a_list[-1]}.gif', save_all=True, append_images=images[1:], duration=60, loop=0)
