import math as m

def sample(x_values: list, y_values: list, N, start, end, f: callable, warnigs: bool = True):
    for i in range(N + 2):
        x = start + i * (end - start) / N
        x_values.append(x)
        y_values.append(f(x))
    if warnigs == True:
        warn_out = 0
        for i, y in enumerate(y_values):
            if m.isnan(y) or m.isinf(y):
                print(f"  ΠΡΟΕΙΔΟΠΟΙΗΣΗ: y[{i}] = {y} στο x = {x_values[i]}")
                warn_out += 1
        if warn_out > 0:
            print(f"  Σύνολο προειδοποιήσεων: {warn_out}")
        else:
            print("Δειγματοληψία OK (χωρίς NaN/inf)")
    return x_values, y_values    

def derivative(x_values: list, N, start, end, f: callable):
    deriv_values = [None] * len(x_values)
    h = (end - start) / N
    for i in range(len(x_values)):
        xi = x_values[i]
        fp = f(xi + h)
        fm = f(xi - h)
        deriv = (fp - fm) / (2 * h)
        deriv_values[i] = deriv
    return deriv_values

def root(x_values: list, y_values: list, f: callable, start, end, N, tollerance: float = 1e-9, epsilon: float = 1e-9, max_iter: int = 100):
    h = (end - start) / N
    def f_prime(x):
        fp = f(x + h)
        fm = f(x - h)
        deriv = (fp - fm) / (2 * h)
        return deriv

    root_guees = []
    root_values = []
    for i in range(len(y_values) - 1):
        if y_values[i] * y_values[i + 1] < 0:
            root_guees.append(x_values[i])
    for i in range(len(root_guees)):
        x0 = root_guees[i]
        for d in range(max_iter):
            y = f(x0)
            y_prime = f_prime(x0) 

            if abs(y_prime) < epsilon:
                break

            x1 = x0 - y / y_prime

            if abs(x1 - x0) < tollerance:
                break

            x0 = x1
        root_values.append(x0)
    return root_values

