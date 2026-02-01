import math 

def sample(f: callable, N, start, end, warnings: bool = True):
    x_values = []
    y_values = []

    for i in range(N + 1):
        x = start + i * (end - start) / N
        x_values.append(x)
        y_values.append(f(x))
    if warnings == True:
        warn_out = 0
        for i, y in enumerate(y_values):
            if math.isnan(y) or math.isinf(y):
                print(f"Sample Warning: y[{i}] = {y} in x = {x_values[i]}")
                warn_out += 1
            if warn_out > 0:
                print(f"Total Warnings: {warn_out}")
            else:
                print("Sample OK!")
    return x_values, y_values