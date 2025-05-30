import ellipse_tools
import numpy as np

import tempfile
from PIL import Image
import glob

## draw a gif of the star at point (a*cos(t), sin(t)) as t varies
#1.3299220317449445
#1.41227364785032 
a = 1.3299220317449445
k = 5
t_list = np.linspace(0.0, 0.25, 500)
steps = 400
with tempfile.TemporaryDirectory() as tmpdir:
    thetas = [2*np.pi*(i/(4*steps)) for i in range(steps+1)]
    rs = [ellipse_tools.min_r_given_theta(t, a) for t in thetas] #[2 for t in thetas]
    min_r = min(rs)
    max_r = max(rs)

    i = 0
    for theta, r in zip(thetas, rs):
        i += 1
        ## transition color from blue to red as r varies from min_r to max_r
        color = (1 - (r-min_r)/(max_r-min_r), 0.3, (r - min_r) / (max_r - min_r))
        ellipse_tools.plot_midpoints(ellipse_tools.return_k_points_d_distance(5, r, theta, a,),a,i,img_name = f"{tmpdir}/{i}.png")
    
    image_files = sorted(glob.glob(f"{tmpdir}/*.png"), key=lambda x: int(x.split('/')[-1].split('.')[0]))

    images = [Image.open(image_file) for image_file in image_files]
    images[0].save(f'gifs/a={a:.3f}_midpoint.gif', save_all=True, append_images=images[1:], duration=100, loop=0)
