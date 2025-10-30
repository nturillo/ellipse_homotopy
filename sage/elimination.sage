R.<a, r, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4> = PolynomialRing(QQ)

# encode ellipse constraints
# ellipse (x/a)^2 + y^2 = 1
p0 = x0^2 + y0^2 * a^2 - a^2
p1 = x1^2 + y1^2 * a^2 - a^2
p2 = x2^2 + y2^2 * a^2 - a^2
p3 = x3^2 + y3^2 * a^2 - a^2
p4 = x4^2 + y4^2 * a^2 - a^2

# distance constraints
d1 = (x0 - x1)^2 + (y0 - y1)^2 - r^2
d2 = (x1 - x2)^2 + (y1 - y2)^2 - r^2
d3 = (x2 - x3)^2 + (y2 - y3)^2 - r^2
d4 = (x3 - x4)^2 + (y3 - y4)^2 - r^2
d5 = (x4 - x0)^2 + (y4 - y0)^2 - r^2

I = ideal(p0, p1, p2, p3, p4, d1, d2, d3, d4, d5)
J = I.elimination_ideal([y1, x1, x2, y2, x3, y3, x4, y4])
locus = J.gens()[0]