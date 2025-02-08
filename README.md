# ellipse_homotopy
Tools for experimentally exploring the homotopy type of Vietoris-Rips complexes generated from ellipses. 

## ellipse_tools: 
misc collection of tools for working with the ellipse

## ripser_ellipse:
script for generating persistance diagram of ellipse

## wf_ellipse:
script for comparing semi-major axis of ellipse $a$ and the smallest $r > 0$ such that the Vietoris-Rips complex of the ellipse at distance $r$ includes a five vertex clique, i.e. $K_5$

## computational_library:
library for wf_ellipse written in C for performance reasons

# Results
Check out r_vs_a.png.
This graph compares the semi-major axis of an ellipse $E$ defined by the function $(\frac{x}{a})^2 + y^2 = 1$ to the smallest $r > 0$ such that $VR(E, r)$ contains $K_5$ as a subgraph.
The function seems to be continuous.

Perhaps more interesting is points_max_loops.png.
This graph shows which point on the ellipse generated 2 loops after 5 steps for each $a$.
Note that we only check points in the 1st quadrant since these are the only points up to symmetry.
The point are labeled 0-99; these labels correspond to the 100 samples taken for $a \in [1, \sqrt(2)]$.
The code checks points in a counter-clockwise direction starting from the rightmost point, so if a point appears on this graph, it's possible that points counter-clockwise of it also generate 2 loops.
Observe that the first 79 points are all towards the bottom of the ellipse.
Then, the last 20 or so are broken up between the very top, kind of in the middle, and the very right.
To me, this is very surprising behaviour.
Maybe some of it is caused by floating point errors?
Something to look into

# Installation/Usage
Optional but recommended:
Create a virtual environment for this python project
```sh
python -m venv venv
source venv/bin/activate
```
This is good practice, but you'll have to run the source command every time you start a new terminal.
To deactivate, either close the terminal instance or run
```sh
deactivate
```

Install the python packages:
```sh
pip install -r requirements.txt
```

Now you can use ellipse_tools and ripser_ellipse!
To use wf_ellipse, you'll need to compile the C library.
First, you'll need to install GSL (GNU Scientific Library) since that is a dependency of the C code.

https://www.gnu.org/software/gsl/

I use Debian on WSL, so if you're on Debian, Ubuntu, or the WSL version of either of those, it's easy!
## Debian, Ubuntu, WSL version of those:
Install GSL
```sh
sudo apt install libgsl-dev
```
Compile C library (assuming you're using gcc, which if you're on linux you probably are. If you know you're not using gcc then I'm sure you can figure it out from the makefile.)
```sh
make
```

## Other OS:
Sorry, you're on your own, but feel free to message me (Nicco) in the discord if you want some help.
If you're really interested in programming, I recommend you check out Linux or WSL.
My life has gotten much easier since using WSL, and it's really easy to set up.


