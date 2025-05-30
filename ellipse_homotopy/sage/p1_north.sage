var('t a d x y')

# Define the symbolic expressions
z = (2 + 2*sqrt(a^4+d^2-a^2*d^2))/(a^2+1-d^2)
s = (z-sqrt(z^2-4))/2
print(s.subs(a=1.2, d=1.9921904610306815))
x_0 = a*(1-s^2)/(1+s^2)
y_0 = (2*s)/(1+s^2)
print(x_0.subs(a=1.2, d=1.9921904610306815))
print(y_0.subs(a=1.2, d=1.9921904610306815))

eq = (x_0 - d/2)^2 + (y_0 - sqrt(1-d^2/(4*a^2)))^2 == d^2
print(eq.lhs().subs(a=1.2, d=1.9921904610306815))
print(eq.rhs().subs(d=1.9921904610306815))

solution = solve(eq, d)
print(str(solution)[:100])
d_expr = solution[0].rhs().simplify_full()
#print(d_expr)
#poly = poly.expand().simplify_full()
#print(poly)
#print(solution[0].lhs().subs(d=1.9921904610306815))
sub = d_expr.subs(a=1.2, d=1.9921904610306815).simplify_full().n()
print(sub)
print(d_expr._latex_())