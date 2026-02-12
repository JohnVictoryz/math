import tkinter as tk
from tkinter import messagebox

from .matplotlib import PlotPanel


def startui(compute_callback):
    root = tk.Tk()
    root.title("Function Explorer")

    controls_frame = tk.Frame(root)
    controls_frame.pack(fill="x", padx=8, pady=8)

    tk.Label(controls_frame, text="Samples").grid(row=0, column=0, sticky="w")
    samples_entry = tk.Entry(controls_frame)
    samples_entry.insert(0, "1000")
    samples_entry.grid(row=0, column=1, padx=4)

    tk.Label(controls_frame, text="X min").grid(row=1, column=0, sticky="w")
    xmin_entry = tk.Entry(controls_frame)
    xmin_entry.insert(0, "-360")
    xmin_entry.grid(row=1, column=1, padx=4)

    tk.Label(controls_frame, text="X max").grid(row=2, column=0, sticky="w")
    xmax_entry = tk.Entry(controls_frame)
    xmax_entry.insert(0, "360")
    xmax_entry.grid(row=2, column=1, padx=4)

    plot_panel = PlotPanel(root)

    def on_plot():
        try:
            samples = int(samples_entry.get())
            xmin = float(xmin_entry.get())
            xmax = float(xmax_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Samples must be an integer and range values must be numbers.")
            return

        if samples <= 0:
            messagebox.showerror("Input Error", "Samples must be greater than zero.")
            return

        if xmin >= xmax:
            messagebox.showerror("Input Error", "X min must be less than X max.")
            return

        try:
            results = compute_callback(samples, xmin, xmax)
            plot_panel.render(
                results.x_values,
                results.y_values,
                results.derivative_values,
                results.root_values,
            )
        except Exception as exc:
            messagebox.showerror("Computation Error", str(exc))

    tk.Button(controls_frame, text="Plot", command=on_plot).grid(row=3, column=0, columnspan=2, pady=8)

    root.mainloop()
