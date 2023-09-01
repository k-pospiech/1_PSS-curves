from scipy.optimize import curve_fit
import numpy as np

def curve_fitting(x_list, y_list):
    """
    Performs curve fitting on given data points using specified curve types.

    Parameters:
    - x_list: list of 1D NumPy arrays
        The x-coordinates of the data points for each data set.
    - y_list: list of 1D NumPy arrays
        The y-coordinates of the data points for each data set.
    
    User Input:
    - The type of curve (polynomial, exponential, logarithmic) to fit for each data set.
    - For polynomial fits, the user also specifies the degree of the polynomial.
    
    Returns:
    - A list of curve coefficients for each data set.
    
    Output:
    - Prints the curve equation in a format that can be used in other Python scripts.
    
    Examples:
    >>> x1 = np.linspace(0, 10, 20)
    >>> y1 = 2 * x1**2 + 1 + np.random.normal(0, 1, len(x1))
    >>> curve_fitting([x1], [y1])
    Select the fit function (polynomial/exponential/logarithmic): polynomial
    Define the polynomial degree: 2
    0.9894x**2 + 0.0248*x + 1.0529
    """

    curve_coefficients = []

    for x, y in zip(x_list, y_list):

        curve_type = input("Select the fit function (polynomial/exponential/logarithmic): ")

        if curve_type == "polynomial":
                
            def curve(x, *coefficients):
                return np.polyval(coefficients, x)
            
            degrees = int(input("Define the polynomial degree: "))  # An example way to define degrees

            p0 = [1] * (degrees + 1)  # Initial guess
        
        elif curve_type == "exponential":

            def curve(x, a, b):
                return a * np.exp(b * x)
            
            p0 = [1,1] # Initial guess

        elif curve_type == "logarithmic":

            def curve(x, a, b):
                return a + b * np.log(x)
            
            p0 = [1,1] # Initial guess

        else:
            raise ValueError("Invalid curve type")
        
        params, _ = curve_fit(curve, x, y, p0=p0)
        curve_coefficients.append(params)

        if curve_type == "polynomial":
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
            print(polynomial)

        elif curve_type == "exponential":
            exponent = f"{params[0]:.4f} x**{params[1]:.4f}"
            print(exponent)

        elif curve_type == "logarithmic":
            logarithm = f"{params[1]:.4f} * log(x) + {params[0]:.4f}"
            logarithm = logarithm.replace(" + -", " - ")
            print(logarithm)

    return curve_coefficients


# Example usage
x1 = np.linspace(1, 10, 10)
y1 = 3 * x1 ** 2 + 2
x2 = np.linspace(1, 10, 10)
y2 = 3 * np.exp(0.3 * x2)
x3 = np.linspace(1, 10, 10)
y3 = 2 + 1.5 * np.log(x3)

a = curve_fitting([x1], [y1])