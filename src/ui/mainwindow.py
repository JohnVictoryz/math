import tkinter as tk
from tkinter import messagebox
from .matplotlib import display_plot

plot_dis = False
def startui(controller):
    global plot_dis
    root = tk.Tk()
    root.title("My Math UI")

    state = tk.BooleanVar()

    tk.Label(root, text="Display math?", font=("Arial", 18)).pack()
    tk.Label(root, text="Type the function please", font=("Arial", 12)).pack()
    func = tk.Text(root, font=("Arial", 12),height = 1, width = 25)
    func.pack()
    tk.Checkbutton(root, text="Show plot", variable=state).pack()

    def on_click():
        global plot_dis        
        #print(f"The text was{func.get('1.0', 'end-1c')}")
        expression = func.get('1.0', 'end-1c')
        try:
            if state.get() == False:
                messagebox.showerror("Info", "You did not check the checkbox", icon='info')
                return
            if state.get() and plot_dis == False:
                x, y, dy, roots = controller.compute(expression, -360, 360)
                display_plot(root, x, y, dy, roots)
                plot_dis = True
            else:
                messagebox.showerror("Warning", "The plot function was called and returned a plot", icon='warning')
        except Exception as e:
            messagebox.showerror("Error", str(e), icon='error')
            plot_dis = False
        #if state.get() and plot_dis == False:
        #    x, y, dy, roots = compute_callback
        #    display_plot(root, x, y, dy, roots)
        #    plot_dis = True
        #elif state.get() == False:
        #    messagebox.showerror("Info", "You did not check the checkbox", icon='info')
        #else:
        #    messagebox.showerror("Warning", "The plot function was called and returned a plot", icon='warning')
    tk.Button(root, text="Ready", command=on_click).pack()

    root.mainloop()
