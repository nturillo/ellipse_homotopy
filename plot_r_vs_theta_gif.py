import ellipse_tools
import numpy as np

import tempfile
from PIL import Image
import glob

import matplotlib.pyplot as plt

## draw the smallest star in the ellipse (x/a)^2 + (y)^2 = 1 as a varies

inflection = 1.3299220317449445
range = 0.001
a_vals = np.linspace(inflection - range, inflection + range, 200)
t_vals = np.linspace(0.0, 0.25, 200)

with tempfile.TemporaryDirectory() as tmpdir:
    for i, a in enumerate(a_vals):
        thetas = ellipse_tools.get_ellipse_points_ts(t_vals, a)
        rs = [ellipse_tools.min_r_given_theta(t, a) for t in thetas]

        ## plot
        fig, ax = plt.subplots()
        #ax.set_xlim(0, np.pi/2)
        y_min = min(rs)
        #ax.set_ylim(y_min, y_min + 1e-7)
        plt.gca().set_yticklabels([])
        ax.plot(thetas, rs)
        plt.xlabel('theta')
        plt.ylabel('r')
        plt.title('r vs theta')
        plt.savefig(f"{tmpdir}/{i}.png")
        plt.close()
   
    image_files = sorted(glob.glob(f"{tmpdir}/*.png"), key=lambda x: int(x.split('/')[-1].split('.')[0]))

    images = [Image.open(image_file) for image_file in image_files]
    ## boomerang effect
    images = images + images[-2:0:-1]
    images[0].save(f'gifs/inflection.gif', save_all=True, append_images=images[1:], duration=60, loop=0)