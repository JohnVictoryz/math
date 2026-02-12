import numpy
import engine as engine
from ui.mainwindow import startui
from asteval import Interpreter


#def f(x): 
#    d = math.radians(x)
#    return (math.sin(d)*math.cos(d*d)) * 0.45

aeval = Interpreter(use_numpy=True)
aeval.symtable['np'] = numpy

function_raw = input("Enter f(x) function: ").replace("^", "**")

func_def = f"def f(x): return {function_raw}"
aeval(func_def)

f = aeval.symtable.get("f")

if f:
    print("Function was Created succesfully")
else:
    print("Error while creating function")

def compute():
    x_values, y_values = engine.sample(f,1000,-360,360)
    deriv_values = engine.derivative(x_values,f)
    root_values = engine.root(x_values,y_values,f)

    return x_values, y_values, deriv_values, root_values

startui(compute())
