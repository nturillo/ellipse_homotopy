# Set ellipse parameters
a = 1.2
b = 1

# Declare variables for unknown points and distance
vars = []
for i in range(1, 5):  # points 1 to 4
    vars.append(var(f'x{i}'))
    vars.append(var(f'y{i}'))
var('d2')

# Known first point
x0 = a
y0 = 0

# Create equations
eqs = []

# Ellipse constraints for points 1 to 4
for i in range(1, 5):
    x = var(f'x{i}')
    y = var(f'y{i}')
    eqs.append((x/a)^2 + (y/b)^2 == 1)

# Distance constraints between adjacent points, including wrap-around
points = [(x0, y0)] + [(var(f'x{i}'), var(f'y{i}')) for i in range(1, 5)]
for i in range(5):
    x1, y1 = points[i]
    x2, y2 = points[(i+1)%5]
    eqs.append((x1 - x2)^2 + (y1 - y2)^2 == d2)

# Solve
sols = solve(eqs, 'x4', solution_dict=True)
sols

print(sols)