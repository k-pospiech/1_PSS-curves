def simple_plot(X, Y, title='Data Plot', xlabel='X', ylabel='Y', annotations = None):
    """
    Plots a simple graph using matplotlib with multiple datasets.

    Parameters:
    - X (list): A list of Pandas Series representing the x-axis data.
    - Y (list): A list of Pandas Series representing the y-axis data.
    - title (str, optional): The title of the plot. Default is 'Data Plot'.
    - xlabel (str, optional): The label for the x-axis. Default is 'X'.
    - ylabel (str, optional): The label for the y-axis. Default is 'Y'.
    - annotations (list, optional): A list of tuples, each containing x and y coordinates for annotation.

    Returns:
    - None: This function only plots the data and doesn't return any value.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10,6))

    # Fonts
    plt.rcParams['font.family'] = 'monospace'
    plt.rcParams['font.monospace'] = ['FreeMono'] + plt.rcParams['font.monospace']

    # Annotations 
    if annotations:
        for (x, y) in annotations:
            plt.annotate(f'({x:.2f}, {y:.2f})', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    # Grids and ticks
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.grid(True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    # Tick fontsize
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)


    for x,y in zip(X,Y):
        plt.plot(x, y, marker='o', markersize=1, linewidth=1, linestyle='-', label=f"Plot for {x.name} vs {y.name}")

    plt.legend(fontsize=12)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.tight_layout()

    # Save the figure at 300 DPI
    plt.savefig(title, dpi=300)

    plt.show()