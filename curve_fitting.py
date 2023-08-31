from scipy.optimize import curve_fit
import numpy as np

def curve(x, *coefficients):
    return np.polyval(coefficients, x)

def curve_fitting(x, y, degree):
    """
    Fits a polynomial curve to given x and y data points and returns the polynomial equation.

    Parameters:
    - x_list (list of array-like): A list of array-like objects representing the x-coordinates for each set of data points.
    - y_list (list of array-like): A list of array-like objects representing the y-coordinates for each set of data points.
    - degrees (list of int): A list of integers specifying the degree of the polynomial to fit for each set of data points.

    Returns:
    - list of tuples: Each tuple contains the following:
        1. array-like: Coefficients of the fitted polynomial for each set of data points.
        2. str: String representation of the polynomial equation in the form "ax^n + bx^(n-1) + ... + k".

    Example usage:
    x1 = np.linspace(0, 10, 20)
    y1 = 2 * x1**2 + 1 + np.random.normal(0, 1, len(x1))
    x2 = np.linspace(0, 10, 20)
    y2 = 3 * x2**3 + 1 + np.random.normal(0, 1, len(x2))

    curve_fitting([x1, x2], [y1, y2], [2, 3])
    """
    params, _ = curve_fit(curve, x, y, p0=[1]*(degree+1))

    terms = []
    for i, coef in enumerate(params):
        if i == len(params) - 1: # Last term, constant
            terms.append(f"{coef:.4f}")
        elif i == len(params) - 2: # Penultimate term, with x
            terms.append(f"{coef:.4f}*x")
        else:
            terms.append(f"{coef:.4f}x**{len(params) - 1 - i}")

    polynomial = " + ".join(terms)
    polynomial = polynomial.replace(" + -", " - ")

    return polynomial

# Example usage
x1 = np.linspace(0, 10, 20)
y1 = 2 * x1**2 + 1 + np.random.normal(0, 1, len(x1))

polynomial = curve_fitting(x1, y1, 2)
print(f"f(x) = {polynomial}")