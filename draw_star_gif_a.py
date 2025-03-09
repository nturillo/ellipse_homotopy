import ellipse_tools
import numpy as np

import tempfile
from PIL import Image
import glob

## draw the smallest star in the ellipse (x/a)^2 + (y)^2 = 1 as a varies

a_list = np.linspace(1.0, 1.2, 50)
k = 5
t_list = np.linspace(0.0, 0.2, 500)

with tempfile.TemporaryDirectory() as tmpdir:
    for i, a in enumerate(a_list):
        min_r = 2.0
        argmin_r = 0.0
        ts_ellipse = ellipse_tools.get_ellipse_points_ts(t_list, a)
        rs = [ellipse_tools.min_r_given_t(t, a) for t in ts_ellipse]
        for i2, r in enumerate(rs):
            if r < min_r:
                min_r = r
                argmin_r = i2
        t = ts_ellipse[argmin_r]
        ellipse_tools.plot_k_points_d_Euclid_apart(k, min_r, t, a, f"{tmpdir}/{i}.png", verbose = False)
   
    image_files = sorted(glob.glob(f"{tmpdir}/*.png"), key=lambda x: int(x.split('/')[-1].split('.')[0]))

    images = [Image.open(image_file) for image_file in image_files]
    ## boomerang effect
    images = images + images[-2:0:-1]
    images[0].save(f'gifs/star_a={a_list[0]}-{a_list[-1]}.gif', save_all=True, append_images=images[1:], duration=200, loop=0)
