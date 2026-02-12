# Function Explorer

A small desktop app to sample, differentiate, find roots, and plot a user-defined function.

## Run

```bash
pip install -r requirements.txt
python src/main.py
```

Then enter an expression for `f(x)` (example: `np.sin(x)`), and use the GUI controls to set:

- sample count
- x min
- x max

Click **Plot** to update the same embedded Matplotlib chart.

## Architecture

- `src/main.py` wires dependencies only.
- `src/engine/model.py` owns compute workflow and returns a `ComputeResult`.
- `src/ui/mainwindow.py` handles input validation and UI-level error dialogs.
- `src/ui/matplotlib.py` owns one persistent figure/canvas and redraws in place.
