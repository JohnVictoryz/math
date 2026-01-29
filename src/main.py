import math as m
import matplotlib.pyplot as plt
def f(x):
    d = m.radians(x)
    return (m.sin(d)*m.cos(d*d)) * 0.45
#def f(x):
 #   return x*x - x*x*x

start = -360
end = 360

N = 3000
x_values = []
y_values = []

for i in range(N + 2):
    x = start + i * (end - start) / N
    x_values.append(x)
    y_values.append(f(x))

warnings = 0
for i, y in enumerate(y_values):
    if m.isnan(y) or m.isinf(y):
        print(f"  ΠΡΟΕΙΔΟΠΟΙΗΣΗ: y[{i}] = {y} στο x = {x_values[i]}")
        warnings += 1

if warnings > 0:
    print(f"  Σύνολο προειδοποιήσεων: {warnings}")
else:
    print("Δειγματοληψία OK (χωρίς NaN/inf)")

h = (end - start) / N
deriv_values = [None] * len(x_values)

for i in range(len(x_values)):
    xi = x_values[i]
    fp = f(xi + h)
    fm = f(xi - h)
    deriv = (fp - fm) / (2 * h)
    deriv_values[i] = deriv

root_values = []
for i in range(len(y_values) - 1):
    if abs(y_values[i]) < 1e-9:
        root_values.append(x_values[i])
    elif y_values[i] * y_values[i + 1] < 0:
        root_values.append(x_values[i])
    
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.plot(x_values, y_values, label='f(x)')
plt.plot(x_values, deriv_values, label='f\'(x)')
plt.legend()
plt.scatter(root_values, [0] * len(root_values), color='red', label='Ρίζες')
plt.show()