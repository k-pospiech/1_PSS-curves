def curve_fitting(x, y, degree=2, graph="Y"):
    """
    Fits a polynomial curve to given x and y data, and optionally plots the curve.

    This function takes in arrays of x and y coordinates, along with the desired degree of the polynomial 
    for curve fitting (default is 2). It returns the coefficients of the fitted polynomial and prints the 
    equation of the curve.

    Optionally, the function can plot the data and the fitted curve. If a fourth argument is passed, 
    plotting is skipped. Otherwise, the user is prompted to input labels for the plot's title, x-axis, 
    and y-axis.

    Parameters:
    -----------
    x : array-like
        Array of x-coordinate values.
    y : array-like
        Array of y-coordinate values.
    degree : int, optional
        Degree of the polynomial curve to be fitted (default is 2).
    graph : str, optional
        Flag to control whether the plot should be displayed ("Y") or skipped (any other value).

    Returns:
    --------
    None
        The function prints the polynomial coefficients and optionally displays a plot.

    Examples:
    ---------
    Without plot:
    >>> import numpy as np
    >>> x = np.linspace(0, 10, 20)
    >>> y = 2*x**2 + 1 + np.random.normal(0, 1, len(x))
    >>> curve_fitting(x, y, 2, 0)
    Fitted Parameters: [2.0597, -0.5979, 2.0846]
    f(x) = 2.0846x^2 - 0.5979x + 2.0597

    With plot:
    >>> import numpy as np
    >>> x = np.linspace(0, 10, 20)
    >>> y = 2*x**2 + 1 + np.random.normal(0, 1, len(x))
    >>> curve_fitting(x, y, 2)
    Fitted Parameters: [2.0021, -0.0077, 0.9736]
    f(x) = 0.9736x^2 - 0.0077x + 2.0021
    Title: Curve Fit
    X label: Current [A]
    Y label: Temperature [degC]
    [Displays plot]
    """
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    # Define the curve function
    def curve(x,*coefficients):
        return np.polyval(coefficients,x)

    # Fit the curve
    params, covariance = curve_fit(curve,x,y,p0=[1]*(degree+1))

    # Prompt parameters
    print("Fitted Parameters: ", params)

    # Display the polynomial in the form: ax**n + bx**(n-1) + ... + k
    #Reverse the coefficients because we want to start from the highest degree.
    coeffs = params[::-1]
    terms = []
    for i, coeff in enumerate(coeffs):
        if i == 0:  #Highest degree term
            terms.append(f"{coeff:.4f}x^{len(coeffs) - 1}")
        elif i == len(coeffs) - 1:  # Constant term
            terms.append(f"{coeff:.4f}")
        else:  #Middle terms
            terms.append(f"{coeff:.4f}x^{len(coeffs) - 1 - i}")

    #Join terms with '+' while handling positive and negative coefficients.
    polynomial = " + ".join(term for term in terms if not term.startswith("0.00"))
    polynomial = polynomial.replace(" + -", " - ")
    print("f(x) = ", polynomial)

    if graph == "Y":
        # Get the title and labels:
        Title = input("Title: ")
        xlabel = input("X label: ")
        ylabel = input("Y label: ")
        # Plot the data and the curve
        plt.scatter(x,y,label="Data")
        plt.plot(x,curve(x,*params),color='red',label="Fitted curve")
        plt.legend()
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(Title)
        plt.grid()
        plt.show()
        return
    else:
        return