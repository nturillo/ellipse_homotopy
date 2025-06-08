import ellipse_tools
import numpy as np
import matplotlib.pyplot as plt


## draw a gif of the star at point (a*cos(t), sin(t)) as t varies
#1.3299220317449445
#1.41227364785032 
important_a = 1.3299220317449445
epsilon = .01
a_min = 1.41
a_max = 1.4142
step = 1000
t_list = np.linspace(0.0, 0.25, 500)

#point
x = .25*np.pi

final_list=[]
color_list=[]

## plot
fig, ax = plt.subplots()
plt.clf()
plt.xlabel('a')
plt.ylabel('r')
plt.title('a vs r')

fig, ax = plt.subplots()
ax.set_xlim(-np.sqrt(2) - 0.1, np.sqrt(2) + 0.1)
ax.set_ylim(-1.1, 1.1)

for i in range(1,step):
    a = a_min + i*(a_max-a_min)/step
    thetas = ellipse_tools.get_ellipse_points_ts(t_list, a)
    rs = [ellipse_tools.min_r_given_theta(t, a) for t in thetas] #[2 for t in thetas]
    max_r = max(rs)
    r_x = ellipse_tools.min_r_given_theta(x, a)
    culur = [max(0,-100*abs(a-important_a)+1), 0.0, max(0,-200*abs(a-important_a)+1)]
    final_list.append([a, (r_x/max_r)])
    color_list.append(culur)

final_list = np.array(final_list)
color_list = np.array(color_list)

ax.scatter(final_list[:,0], final_list[:,1],s=1, c = color_list)
plt.autoscale() 
plt.savefig(f'images/a_vs_r_min={a_min}_max={a_max}_point.png')