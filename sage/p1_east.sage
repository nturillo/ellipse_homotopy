var('t a d x y')

# Define the symbolic expressions
s2 = (d^2 - 2 + 2*sqrt(1-d^2+d^2*a^2))/(4*a^2 - d^2)
s = sqrt(s2)
print(s.subs(a=1.2, d=1.9921814))
x_0 = a*(1-s^2)/(1+s^2)
y_0 = (2*s)/(1+s^2)
print(x_0.subs(a=1.2, d=1.9921814))
print(y_0.subs(a=1.2, d=1.9921814))

eq = (x_0 - a*sqrt(1-d^2/4))^2 + (y_0 + d/2)^2 == d^2
print(eq)
print(eq.lhs().subs(a=1.2, d=1.9921815))
print(eq.rhs().subs(d=1.9921815))

solution = solve(eq, d)
print(str(solution)[:100])
d_expr = solution[0].rhs()
print(solution[0].lhs().subs(d=1.9921814))
sub = d_expr.subs(a=1.2, d=1.9921814).simplify_full().n()
print(sub)