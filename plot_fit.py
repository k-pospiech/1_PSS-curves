import matplotlib.pyplot as plt
import numpy as np

def plot_fit(x_data, y_data, coefficients, curve_type):

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

from curve_fitting import curve_fitting

# Example usage
x1 = np.linspace(1, 10, 10)
y1 = 3 * x1 ** 2 + 2
x2 = np.linspace(1, 10, 10)
y2 = 3 * np.exp(0.3 * x2)
x3 = np.linspace(1, 10, 10)
y3 = 2 + 1.5 * np.log(x3)

fit_info = curve_fitting([x1], [y1])

for info in fit_info:
    plot_fit(info['x_data'], info['y_data'], info['coefficients'], info['curve_type'])