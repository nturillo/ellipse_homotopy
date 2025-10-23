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

import numpy as np
Rr.<r> = PolynomialRing(QQ)
a_vals = [132/100, 134/100, 140/100, 1414/1000]
for a_val in a_vals:
    north_locus_r = Rr(north_locus.subs(a=a_val))
    east_locus_r = Rr(east_locus.subs(a=a_val))
    north_roots = north_locus_r.roots(ring=RR)
    east_roots = east_locus_r.roots(ring=RR)

    threshold = (4 * sqrt(3) * a_val^2) / (3 *a_val^2 + 1) + 0.00000001 
    #print(f"threshold: {threshold.n()}")
    #print(f"North roots: {north_roots}")
    #print(f"East roots: {east_roots}")
    #north_roots_filtered = [r for r in north_roots if r[0] > threshold]
    #east_roots_filtered = [r for r in east_roots if r[0] > threshold]
    #print(f"North roots filtered: {north_roots_filtered}")
    #print(f"East roots filtered: {east_roots_filtered}")
    north_root = find_root(north_locus_r, threshold, 10.0, xtol=1e-12)
    east_root = find_root(east_locus_r, threshold, 10.0, xtol=1e-12)

    print(f"a_val: {a_val}")
    #print(f"north_roots: {north_roots_filtered}")
    #print(f"east_roots: {east_roots_filtered}")
    D = north_root - east_root
    print(f"D: {D}")