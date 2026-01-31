import math as m

def sample(N, start, end, f: callable, warnigs: bool = True):
    x_values = []
    y_values = []
        
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

def root(
    x_values: list,
    y_values: list,
    f: callable,
    tolerance: float = 1e-9,
    epsilon: float = 1e-12,
    max_iter: int = 50
):
    # Numerical derivative step (independent of sampling)
    h = 1e-6

    def f_prime(x):
        return (f(x + h) - f(x - h)) / (2 * h)

    # 1. Find bracketing intervals
    brackets = []
    for i in range(len(y_values) - 1):
        if y_values[i] * y_values[i + 1] < 0:
            a = x_values[i]
            b = x_values[i + 1]
            brackets.append((a, b))

    roots = []

    # 2. Solve each bracket
    for (a, b) in brackets:
        # Start Newton at midpoint
        x = 0.5 * (a + b)

        converged = False

        for _ in range(max_iter):
            fx = f(x)
            dfx = f_prime(x)

            # Newton step only if derivative is safe
            if abs(dfx) > epsilon:
                x_new = x - fx / dfx

                # Accept Newton step only if it stays inside bracket
                if a < x_new < b:
                    if abs(x_new - x) < tolerance and abs(f(x_new)) < tolerance:
                        x = x_new
                        converged = True
                        break
                    x = x_new
                    continue

            # ---- Bisection fallback ----
            c = 0.5 * (a + b)
            fc = f(c)

            if abs(fc) < tolerance or (b - a) < tolerance:
                x = c
                converged = True
                break

            if f(a) * fc < 0:
                b = c
            else:
                a = c

            x = 0.5 * (a + b)

        # 3. Accept root only if verified
        if converged and abs(f(x)) < tolerance:
            # Deduplicate
            if not any(abs(x - r) < 1e-6 for r in roots):
                roots.append(x)
        else:
            print(f"⚠️ Failed to converge in bracket [{a}, {b}]")

    return roots
