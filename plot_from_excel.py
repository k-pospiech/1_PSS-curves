def plot_from_excel():
    """
    Fetches data from an Excel worksheet and plots it using simple_plot function.
    
    This function will ask the user to manually select the columns with X and Y values.
    Afterward, it plots the selected data columns. User can select multiple data columns.
    
    Parameters:
    - None

    Returns:
    - None: This function only plots the data and doesn't return any value.
    
    Note:
    - Make sure the data_from_worksheet and simple_plot functions are accessible.
    - The user will interactively choose the columns for X and Y axis data.
    """
    from data_from_worksheet import data_from_worksheet
    from simple_plot import simple_plot
    import numpy as np

    folder = "D:\Python_Projects\PSS-curves\Inputs"
    spreadsheet = "0_5mm2_Correlations.xlsx"
    worksheet = "Insulation_0"

    X=[]
    Y=[]

    data = data_from_worksheet(folder, spreadsheet, worksheet)
    
    # Show columns with 1-based numbering for easier user input
    for idx, column_name in enumerate(data.columns, start=1):
        print(f"{idx}. {column_name}")

    # Ask for user input
    X_input = int(input("Please select the column (1/2/3/...) with X values: "))
    Y_input = int(input("Please select the column (1/2/3/...) with Y values: "))

    # Extract the chosen columns from the data and append to X and Y lists
    Chosen_X_header = data.columns[X_input-1]
    Chosen_Y_header = data.columns[Y_input-1]

    X.append(data[Chosen_X_header])
    Y.append(data[Chosen_Y_header])

    # Ask user for more inputs
    more = input("Press '1' to add more data or any other key to quit: ")

    while more == '1':

        # Show columns with 1-based numbering for easier user input
        for idx, column_name in enumerate(data.columns, start=1):
            print(f"{idx}. {column_name}")

        # Ask for user input
        X_input = int(input("Please select the column (1/2/3/...) with X values: "))
        Y_input = int(input("Please select the column (1/2/3/...) with Y values: "))

        # Extract the chosen columns from the data and append to X and Y lists
        Chosen_X_header = data.columns[X_input-1]
        Chosen_Y_header = data.columns[Y_input-1]

        X.append(data[Chosen_X_header])
        Y.append(data[Chosen_Y_header])

        more = input("Press '1' to add more data or any other key to quit: ")

    # print(X, Y)

    simple_plot(X, Y, title="Data from Excel")

plot_from_excel()