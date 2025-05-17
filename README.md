# ellipse_homotopy
Tools for experimentally exploring the homotopy type of Vietoris-Rips complexes generated from ellipses. 

# Code Structure
Some of the high-performace code is written in C in the file computational_library.c.
Wrappers for that as well as some other tools are in ellipse_tools.py.

All the other python files are scripts written to do specific things using functions from ellipse_tools.

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
Compile C library
```sh
make
```

## Other OS:
Sorry, you're on your own, but feel free to message me (Nicco) in the discord if you want some help.
If you're really interested in programming, I recommend you check out Linux or WSL.
My life has gotten much easier since using WSL, and it's really easy to set up.


