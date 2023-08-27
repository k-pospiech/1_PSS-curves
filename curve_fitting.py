"""
This function returns the polynomial coefficients, and plots the curve based on the provided x and y data, 
and the degree of polynomial that should be used (default 2nd degree)

In the process, it will also ask for input to create the proper graph (accepts empty strings to skip labels completely).
If any 4th argument is passed, it will skip the plotting step

    Example without plot:
>>> import numpy as np
>>> x = np.linspace(0,10,20)
>>> y = 2*x**2 + 1 + np.random.normal(0,1,len(x))
>>> curve_fitting(x,y,2,0)

Fitted Parameters:  [ 2.05971003 -0.59791269  2.08456956]
f(x) =  2.0846x^2 - 0.5979x^1 + 2.0597

    Example with plot:
>>> import numpy as np
>>> x = np.linspace(0,10,20)
>>> y = 2*x**2 + 1 + np.random.normal(0,1,len(x))
>>> curve_fitting(x,y,2)

Fitted Parameters:  [ 2.00206363 -0.00772845  0.97363155]
f(x) =  0.9736x^2 - 0.0077x^1 + 2.0021
Title: Curve Fit
X label: Current [A]
Y label: Temperature [degC]
    plus pop-up window with the described plot
"""

def curve_fitting(x, y, degree=2, graph="Y"):
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