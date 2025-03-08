import ellipse_tools
import numpy as np

import tempfile
from PIL import Image
import glob

a = 1.2
k = 5
t_list = np.linspace(0.0, 0.25, 100)

with tempfile.TemporaryDirectory() as tmpdir:
    for i, t in enumerate(t_list):
        t_ellipse = ellipse_tools.get_ellipse_points_ts(np.array([t]), a)[0]
        d = ellipse_tools.min_r_given_t(t, a)
        ellipse_tools.plot_k_points_d_Euclid_apart(k, d, t, a, f"{tmpdir}/{i}.png", verbose = False)
    
    image_files = sorted(glob.glob(f"{tmpdir}/*.png"), key=lambda x: int(x.split('/')[-1].split('.')[0]))

    images = [Image.open(image_file) for image_file in image_files]
    images[0].save(f'star_a={a}.gif', save_all=True, append_images=images[1:], duration=100, loop=0)
