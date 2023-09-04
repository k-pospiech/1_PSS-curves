def simple_plot(X, Y, title='Data Plot', xlabel='X', ylabel='Y'):
    """
    Plots a simple graph using matplotlib with multiple datasets.

    Parameters:
    - X (list): A list of Pandas Series representing the x-axis data.
    - Y (list): A list of Pandas Series representing the y-axis data.
    - title (str, optional): The title of the plot. Default is 'Data Plot'.
    - xlabel (str, optional): The label for the x-axis. Default is 'X'.
    - ylabel (str, optional): The label for the y-axis. Default is 'Y'.

    Returns:
    - None: This function only plots the data and doesn't return any value.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10,6))

    for x,y in zip(X,Y):
        plt.plot(x, y, marker='o', markersize=1, linewidth=1, linestyle='-', label=f"Plot for {x.name} vs {y.name}")

    plt.legend()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()