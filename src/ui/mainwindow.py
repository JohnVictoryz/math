import tkinter as tk
from .matplotlib import display_plot

def startui(compute_callback):
    root = tk.Tk()
    root.title("My Math UI")

    state = tk.BooleanVar()

    tk.Label(root, text="Display math?", font=("Arial", 18)).pack()
    tk.Checkbutton(root, text="Show plot", variable=state).pack()

    def on_click():
        if state.get():
            x, y, dy, roots = compute_callback
            display_plot(root, x, y, dy, roots)

    tk.Button(root, text="Ready", command=on_click).pack()

    root.mainloop()
