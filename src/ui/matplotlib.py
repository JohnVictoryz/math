from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class PlotPanel:
    def __init__(self, root):
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def render(self, x_values, y_values, deriv_values, root_values):
        self.axes.clear()
        self.axes.axvline(x=0)
        self.axes.axhline(y=0)
        self.axes.plot(x_values, y_values, label="f(x)")
        self.axes.plot(x_values, deriv_values, label="f'(x)")
        self.axes.scatter(root_values, [0] * len(root_values), color="red", label="Roots")
        self.axes.legend()
        self.canvas.draw()
