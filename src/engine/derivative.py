def derivative(x_values: list, f: callable):
    deriv_values = [None] * len(x_values)
    h = 1e-6
    for i in range(len(x_values)):
        xi = x_values[i]
        fp = f(xi + h)
        fm = f(xi - h)
        deriv = (fp - fm) / (2 * h)
        deriv_values[i] = deriv
    return deriv_values