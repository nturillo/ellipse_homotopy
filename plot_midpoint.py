import ellipse_tools
import numpy as np
import matplotlib.pyplot as plt
import tempfile


## draw a gif of the star at point (a*cos(t), sin(t)) as t varies
#1.3299220317449445
#1.41227364785032 
a = 1.3
k = 5
t_list = np.linspace(0.0, 0.25, 500)

mdpoint = []
colorList = []
steps = 20000

## fix the axis limits
fig, ax = plt.subplots()
ax.set_xlim(-np.sqrt(2) - 0.1, np.sqrt(2) + 0.1)
ax.set_ylim(-1.1, 1.1)

## plot the ellipse as a thin black line
t = np.linspace(0, 2*np.pi, 100)
ax.plot(a*np.cos(t), np.sin(t), 'k')


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
        md = ellipse_tools.midpoint(ellipse_tools.return_k_points_d_distance(5, r, theta, a,))

        mdpoint.append((md[0],md[1]))
        colorList.append(color)
mdpoint = np.array(mdpoint)
colorList = np.array(colorList)
ax.scatter(mdpoint[:,0], mdpoint[:,1],s=1, c = colorList[:,0])

plt.savefig(f"images/midpoints_a={a:.5f}.png")