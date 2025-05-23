import ellipse_tools
import numpy as np

import tempfile
from PIL import Image
import glob

## draw a gif of the star at point (a*cos(t), sin(t)) as t varies

a = 1.35 #1.3299220317449445
k = 5
t_list = np.linspace(0.0, 0.25, 75)

with tempfile.TemporaryDirectory() as tmpdir:
    thetas = ellipse_tools.get_ellipse_points_ts(t_list, a)
    rs = [ellipse_tools.min_r_given_theta(t, a, num_steps=3, num_loops=1) for t in thetas]
    min_r = min(rs)
    max_r = max(rs)

    i = 0
    for theta, r in zip(thetas, rs):
        i += 1
        ## transition color from blue to red as r varies from min_r to max_r
        color = 'blue' #(1 - (r-min_r)/(max_r-min_r), 0.3, (r - min_r) / (max_r - min_r))
        ellipse_tools.plot_k_points_d_Euclid_apart(3, r, theta, a, img_name = f"gifs/triangle/{i}.png", plot_foci=False ,verbose = False, star_color = color)
    
    image_files = sorted(glob.glob(f"{tmpdir}/*.png"), key=lambda x: int(x.split('/')[-1].split('.')[0]))

    images = [Image.open(image_file) for image_file in image_files]
    ## boomerang effect
    images = images + images[-2:0:-1]
    #images[0].save(f'gifs/triangle_a={a:.3f}.gif', save_all=True, append_images=images[1:], duration=70, loop=0)
