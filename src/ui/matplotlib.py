from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def display_plot(root, x_values, y_values, deriv_values, root_values):
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    ax.axvline(x=0)
    ax.axhline(y=0)
    ax.plot(x_values, y_values, label="f(x)")
    ax.plot(x_values, deriv_values, label="f'(x)")
    ax.scatter(root_values, [0]*len(root_values), color="red", label="Roots")
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)