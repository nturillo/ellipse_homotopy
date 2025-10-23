import numpy as np
import ellipse_tools

# This code finds the value of a such that the minimum radius at the North Pole is equal to the minimum radius at the East Pole.

min_a = 1.2 #1.405
max_a = 1.4 #np.sqrt(2)

while (max_a - min_a) > 1e-15:
    a = (min_a + max_a) / 2
    north_r = ellipse_tools.min_r_given_theta(theta=np.pi/2, a=a)
    east_r = ellipse_tools.min_r_given_theta(theta=0, a=a)
    if north_r > east_r:
        min_a = a
    else:
        max_a = a
print(f"a: {a}, min_r(North_Pole): {north_r}, min_r(East_Pole): {east_r}")

# draw ellipse with both stars
draw_stars = False

if draw_stars:
    import matplotlib.pyplot as plt
    ## fix the axis limits
    fig, ax = plt.subplots()
    ax.set_xlim(-np.sqrt(2) - 0.1, np.sqrt(2) + 0.1)
    ax.set_ylim(-1.1, 1.1)
    ## plot the ellipse as a thin black line
    t = np.linspace(0, 2*np.pi, 100)
    ax.plot(a*np.cos(t), np.sin(t), 'k')

    for (theta, d) in zip([0, np.pi/2], [east_r, north_r]):
        x_0, y_0 = (a*np.cos(theta), np.sin(theta))
        num_steps = 5
        points = [(x_0, y_0)]
        for i in range(num_steps):
            (x, y) = ellipse_tools.find_d_distance_point_on_ellipse(d, points[i][0], points[i][1], a)
            points.append((x, y))

        ## plot the points on the ellipse labelled by the step
        points = np.array(points)
        ax.scatter(points[:,0], points[:,1])
        for i, txt in enumerate(range(num_steps)):
            plt.annotate(txt, (points[i,0], points[i,1]))
        #ax.axis('equal')

        ## draw lines between points
        ax.plot(points[:,0], points[:,1], color="red" if theta == 0 else "blue")

    ## save plot
    plt.savefig("images/equal_stars.png")