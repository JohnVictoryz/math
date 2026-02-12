from asteval import Interpreter
import numpy as np
import engine

class Controller:
    def __init__(self):
        self.aeval = Interpreter(use_numpy=True)
        self.aeval.symtable['np'] = np
    
    def build_expression(self, expression):
        expression = expression.replace("^", "**")
        func = f"def f(x): return {expression}"

        self.aeval(func)
        f = self.aeval.symtable.get("f")

        if f is None:
            raise ValueError("Invalid syntax")
        
        return f
    
    def compute(self, expression, start, end, samples=1000):
        f = self.build_expression(expression)

        x, y = engine.sample(f, samples, start, end)
        dy = engine.derivative(x, f)
        roots = engine.root(x, y, f)

        return x, y, dy, roots