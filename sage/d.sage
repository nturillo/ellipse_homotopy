R.<a, r, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4> = PolynomialRing(QQ)

# encode ellipse constraints
# ellipse (x/a)^2 + y^2 = 1
p1 = x1^2 + y1^2 * a^2 - a^2
p2 = x2^2 + y2^2 * a^2 - a^2
p3 = x3^2 + y3^2 * a^2 - a^2
p4 = x4^2 + y4^2 * a^2 - a^2

# east pole
e_p01 = x0 - a
e_p02 = y0

# north pole
n_p01 = x0
n_p02 = y0 - 1

# distance constraints
d1 = (x0 - x1)^2 + (y0 - y1)^2 - r^2
d2 = (x1 - x2)^2 + (y1 - y2)^2 - r^2
d3 = (x2 - x3)^2 + (y2 - y3)^2 - r^2
d4 = (x3 - x4)^2 + (y3 - y4)^2 - r^2
d5 = (x4 - x0)^2 + (y4 - y0)^2 - r^2

# symmetries for east pole star
e_s11 = x2 - x3
e_s12 = y2 + y3
e_s21 = x1 - x4
e_s22 = y1 + y4

# symmetries for north pole star
n_s11 = y1 - y4
n_s12 = x1 + x4
n_s21 = y2 - y3
n_s22 = x2 + x3

north_I = ideal(n_p01, n_p02, p1, p2, p3, p4, d1, d2, d3, d4, d5, n_s11, n_s12, n_s21, n_s22)
north_J = north_I.elimination_ideal([x0, y0, y1, x1, x2, y2, x3, y3, x4, y4])
north_locus = north_J.gens()[0]
print("North locus:")
print(north_locus)
#print(latex(north_locus))

east_I = ideal(e_p01, e_p02, p1, p2, p3, p4, d1, d2, d3, d4, d5, e_s11, e_s12, e_s21, e_s22)
east_J = east_I.elimination_ideal([x0, y0, y1, x1, x2, y2, x3, y3, x4, y4])
east_locus = east_J.gens()[0]
print("East locus:")
#print(latex(east_locus))
print(east_locus)

from sage.rings.polynomial.complex_roots import complex_roots
from sage.rings.polynomial.real_roots import *
import numpy as np
Qr.<r> = PolynomialRing(QQ)
a_vals = [132/100, 134/100, 140/100, 1414/1000]
for a_val in a_vals:
    north_locus_r = Qr(north_locus.subs(a=a_val))
    east_locus_r = Qr(east_locus.subs(a=a_val))
    tolerance = 0.001
    north_roots = real_roots(north_locus_r, retval='interval', max_diameter=tolerance)
    east_roots = real_roots(east_locus_r, retval='interval', max_diameter=tolerance)

    threshold = RR((4 * sqrt(3) * a_val^2) / (3 *a_val^2 + 1))
    #print(f"threshold: {threshold.n()}")
    #print(f"North roots: {north_roots}")
    #print(f"East roots: {east_roots}")
    #north_roots_filtered = [r for r in north_roots if r[0] > threshold]
    #east_roots_filtered = [r for r in east_roots if r[0] > threshold]
    #print(f"North roots filtered: {north_roots_filtered}")
    #print(f"East roots filtered: {east_roots_filtered}")
    north_root = north_roots[6][0]
    east_root = east_roots[6][0]

    print(f"a_val: {a_val.n()}")
    #print(f"north_roots: {north_roots_filtered}")
    #print(f"east_roots: {east_roots_filtered}")
    D = north_root - east_root
    print(f"D: {D}")
    if D.contains_zero():
        print("Panic! We aren't sure if D is positive or negative")
    else:
        print("We're sure about the sign of D thanks to the root bounds")