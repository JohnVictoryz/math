import math as m
import matplotlib.pyplot as plt
import lib.math as engine

def f(x): 
    d = m.radians(x)
    return (m.sin(d)*m.cos(d*d)) * 0.45
#def f(x):
 #   return x*x - x*x*x

x_values, y_values = engine.sample(1000,-360,360,f)
deriv_values = engine.derivative(x_values,f)
root_values = engine.root(x_values,y_values,f)

plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.plot(x_values, y_values, label='f(x)')
plt.plot(x_values, deriv_values, label='f\'(x)')
plt.legend()
plt.scatter(root_values, [0] * len(root_values), color='red', label='Ρίζες')
plt.show()
