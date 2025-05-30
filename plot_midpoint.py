import ellipse_tools
import numpy as np
import matplotlib.pyplot as plt
import tempfile


class point:
    def __init__(self,x,y,color):
        self.xpos = x
        self.ypos = y
        self.color = color

## draw a gif of the star at point (a*cos(t), sin(t)) as t varies
#1.3299220317449445
#1.41227364785032 
a = 1.2
k = 5
t_list = np.linspace(0.0, 0.25, 500)

mdpoint = []
steps = 50000

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

        mdpoint.append(point(md[0],md[1],color))

for P in mdpoint:
    ax.scatter(P.xpos, P.ypos, s=1, color = P.color)

plt.savefig(f"images/midpoints_a={a:.5f}.png")