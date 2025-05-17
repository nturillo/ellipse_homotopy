R.<a, r, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4> = PolynomialRing(QQ)

# encode ellipse constraints
# ellipse (x/a)^2 + y^2 = 1
p0 = x0^2 + y0^2 * a^2 - a^2
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

I = ideal(p0, p1, p2, p3, p4, d1, d2, d3, d4, d5)
J = I.elimination_ideal([x0, y0, y1, x1, x2, y2, x3, y3, x4, y4])
locus = J.gens()[0]

north_I = ideal(n_p01, n_p02, p1, p2, p3, p4, d1, d2, d3, d4, d5, n_s11, n_s12, n_s21, n_s22)
north_J = north_I.elimination_ideal([x0, y0, y1, x1, x2, y2, x3, y3, x4, y4])
north_locus = north_J.gens()[0]

east_I = ideal(e_p01, e_p02, p1, p2, p3, p4, d1, d2, d3, d4, d5, e_s11, e_s12, e_s21, e_s22)
east_J = east_I.elimination_ideal([x0, y0, y1, x1, x2, y2, x3, y3, x4, y4])
east_locus = east_J.gens()[0]