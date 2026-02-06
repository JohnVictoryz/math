import tkinter as tk
from tkinter import messagebox
from .matplotlib import display_plot

plot_dis = False
def startui(compute_callback):
    global plot_dis
    root = tk.Tk()
    root.title("My Math UI")

    state = tk.BooleanVar()

    tk.Label(root, text="Display math?", font=("Arial", 18)).pack()
    tk.Checkbutton(root, text="Show plot", variable=state).pack()

    def on_click():
        global plot_dis
        if state.get() and plot_dis == False:
            x, y, dy, roots = compute_callback
            display_plot(root, x, y, dy, roots)
            plot_dis = True
        else:
            messagebox.showerror("Warning", "The plot function was called and returned a plot")
    tk.Button(root, text="Ready", command=on_click).pack()

    root.mainloop()
