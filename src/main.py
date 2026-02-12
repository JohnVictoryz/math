import numpy
from asteval import Interpreter

from engine import MathModel
from ui.mainwindow import startui


def build_function():
    aeval = Interpreter(use_numpy=True)
    aeval.symtable["np"] = numpy

    function_raw = input("Enter f(x) function: ").replace("^", "**")
    func_def = f"def f(x): return {function_raw}"
    aeval(func_def)

    f = aeval.symtable.get("f")
    if f is None:
        raise ValueError("Error while creating function")

    print("Function was created successfully")
    return f


def main():
    function = build_function()
    model = MathModel(function)
    startui(model.compute)


if __name__ == "__main__":
    main()
