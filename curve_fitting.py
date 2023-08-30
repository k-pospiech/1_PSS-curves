import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def evaluate_polynomial(x, coefficients):
    y = 0
    for i, coef in enumerate(reversed(coefficients)):
        y += coef * (x ** i)
    return y

def curve_fitting(x_list, y_list, degrees, graph="Y", Title="Curve Fit", xlabel="X", ylabel="Y", annotations=None):
    def curve(x, *coefficients):
        return np.polyval(coefficients, x)
    
    plt.figure()

    curve_coefficients = []

    for x, y, degree in zip(x_list, y_list, degrees):
        params, _ = curve_fit(curve, x, y, p0=[1] * (degree + 1))
        curve_coefficients.append(params)  # Store curve coefficients for later use
        if graph == "Y":
            plt.scatter(x, y, label=f"Data {degrees.index(degree) + 1}")
            plt.plot(x, curve(x, *params), label=f"Fitted curve {degrees.index(degree) + 1}")


# # Adding annotations
#     if annotations:
#         for x_annotate, y_annotate, text in annotations:
#             plt.annotate(text, (x_annotate, y_annotate),
#                          textcoords="offset points",
#                          xytext=(0, 10),
#                          ha='center')

# # Dashed Lines (Asymptotes)
#     # Each tuple in the list represents (value, color, linestyle, label)
#     horizontal_lines = [(25, 'g', '--', 'Horizontal Line at y=25'),
#                         (60, 'm', '-.', 'Horizontal Line at y=60')]

#     vertical_lines = [(2, 'r', '--', 'Vertical Line at x=2'),
#                     (8, 'c', '-.', 'Vertical Line at x=8')]

#     # Draw horizontal lines
#     for y_value, color, linestyle, label in horizontal_lines:
#         plt.axhline(y=y_value, color=color, linestyle=linestyle, label=label)

#     # Draw vertical lines
#     for x_value, color, linestyle, label in vertical_lines:
#         plt.axvline(x=x_value, color=color, linestyle=linestyle, label=label)


    # Specific points on curves to annotate
    # Define x_values_to_mark
    x_values_to_mark = {
        # 0: [2, 6],  # x-values for the first curve
        # 1: [3, 7],  # x-values for the second curve
        0: [8],  # x-values for the first curve
        1: [4],  # x-values for the second curve
    }

    for curve_index, x_values in x_values_to_mark.items():
        coefficients = curve_coefficients[curve_index]
        for x_value in x_values:
            y_value = round(evaluate_polynomial(x_value, coefficients),2)
            plt.plot([x_value, x_value], [0, y_value], linestyle='--', color='magenta')
            plt.plot([0, x_value], [y_value, y_value], linestyle='--', color='magenta')
            
            plt.annotate(f"{x_value}", (x_value, 0),
                        textcoords="offset points",
                        xytext=(4, -4),
                        va='top', ha='center',
                        color='magenta')

            plt.annotate(f"{y_value}", (0, y_value),
                        textcoords="offset points",
                        xytext=(-1, 0),
                        va='center', ha='right',
                        color='magenta')


    if graph == "Y":
        plt.legend()
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(Title)
        plt.grid()
        plt.show()

# Example usage
x1 = np.linspace(0, 10, 20)
y1 = 2 * x1**2 + 1 + np.random.normal(0, 1, len(x1))

x2 = np.linspace(0, 10, 20)
y2 = 3 * x2**3 + 1 + np.random.normal(0, 1, len(x2))

# Define annotations as a list of tuples (x_annotate, y_annotate, "Annotation text")
annotations = [(2, 40, "Point A"), (4, 60, "Point B")]

curve_fitting([x1, x2], [y1, y2], [2, 3], annotations=annotations)