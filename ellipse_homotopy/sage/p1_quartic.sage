var('t a d x y')

# Define the symbolic expressions
s = (d^2 - 2 + 2*sqrt(1-d^2+a^2*d^2))/(4*a^2 - d^2)
x_0 = a*(1-s^2)/(1+s^2)
y_0 = (2*s)/(1+s^2)

# Define the equation
eq = t^4*(d^2-2*x*d) + (4*a^2*y*d)*(t^3 + t) + (4*a^2*d^2-2*d^2)*t^2 + (2*x*d+d^2) == 0

# Solve the equation symbolically
solutions = solve(eq, t)

# Substituting the values for a, d, x_0, and y_0 into the solution
x_0_val = x_0.subs(a=1.1, d=1.9)
y_0_val = y_0.subs(a=1.1, d=1.9)

# Take the first solution from the solve results
sol = solutions[1]

# Substitute the values of a, d, x_0, and y_0 into the solution
final_value = sol.subs(a=1.1, d=1.9, x=x_0_val, y=y_0_val)

# Convert to a decimal
print(final_value)  # To get the decimal result
