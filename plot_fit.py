import matplotlib.pyplot as plt
import numpy as np

def plot_fit(x_data, y_data, coefficients, curve_type):
    """
    Plots the fitted curve alongside the original data points. 
    Compatible with the output from the `curve_fitting` function.

    Parameters:
    -----------
    x_data : numpy.ndarray
        The x-coordinates of the data points.
        
    y_data : numpy.ndarray
        The y-coordinates of the data points.
        
    coefficients : list or numpy.ndarray
        The coefficients of the fitted curve. 
        For a polynomial fit, this would be the coefficients of the polynomial 
        starting from the highest degree term.
        
    curve_type : str
        The type of curve used for fitting. 
        "1" for Polynomial, "2" for Exponential, "3" for Logarithmic.

    Example Usage:
    --------------
    >>> plot_fit(np.array([1, 2, 3]), np.array([1, 4, 9]), [1, 0, 0], "1")

    Notes:
    ------
    - This function raises a ValueError for an invalid 'curve_type'.
    - Designed to work seamlessly with the output dictionary from the `curve_fitting` function.

    """
    plt.scatter(x_data, y_data, label='Data Points', color='b')

    x_fit = np.linspace(min(x_data), max(x_data), 500)

    if curve_type == "1": # polynomial
        y_fit = np.polyval(coefficients, x_fit)

    elif curve_type == "2": # exponential
        y_fit = coefficients[0] * np.exp(coefficients[1] * x_fit)

    elif curve_type == "3": # logarithmic
        y_fit = coefficients[0] + coefficients[1] * np.log(x_fit)

    else:
        raise ValueError("Invalid curve type")
    
    plt.plot(x_fit, y_fit, label='Fitted curve', color='r')
    plt.legend()
    plt.title(f'{curve_type.capitalize()} Curve Fitting')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

# # Example usage
# from curve_fitting import curve_fitting

# # Example usage
# x1 = np.linspace(1, 10, 10)
# y1 = 3 * x1 ** 2 + 2

# fit_info = curve_fitting([x1], [y1])

# for info in fit_info:
#     plot_fit(info['x_data'], info['y_data'], info['coefficients'], info['curve_type'])