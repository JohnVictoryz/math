import math
import matplotlib.pyplot as plt
import engine as engine
from ui.mainwindow import startui

def f(x): 
    d = math.radians(x)
    return (math.sin(d)*math.cos(d*d)) * 0.45
#def f(x):
 #   return x*x - x*x*x


def compute():
    x_values, y_values = engine.sample(f,1000,-360,360)
    deriv_values = engine.derivative(x_values,f)
    root_values = engine.root(x_values,y_values,f)

    return x_values, y_values, deriv_values, root_values

startui(compute())