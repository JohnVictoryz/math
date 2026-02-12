from dataclasses import dataclass

from .derivative import derivative
from .root import root
from .sample import sample


@dataclass
class ComputeResult:
    x_values: list[float]
    y_values: list[float]
    derivative_values: list[float]
    root_values: list[float]


class MathModel:
    def __init__(self, function: callable):
        self.function = function

    def compute(self, samples: int, xmin: float, xmax: float) -> ComputeResult:
        x_values, y_values = sample(self.function, samples, xmin, xmax)
        derivative_values = derivative(x_values, self.function)
        root_values = root(x_values, y_values, self.function)
        return ComputeResult(x_values, y_values, derivative_values, root_values)
