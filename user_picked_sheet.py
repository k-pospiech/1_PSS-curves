def user_picked_sheet(folder):
    """
    This function takes the path to the Input folder and lets user manually pick the worksheet from the .xls, .xlsx or .csv files inside to extract the data
    It involves numerical choice so the usedr doesn't need to retype the file/worksheet name manually, and has basic error handling to ensure valid input

    Example:
    >>> folder = "D:\Python_Projects\PSS-curves\Inputs"
    >>> a = user_picked_sheet(folder)
    >>> print(a.head(5))

    Available Spreadsheets:
    1. ANSYS120mm2Copper_Profile.xls
    2. Input.xlsx
    3. Template.xlsx
    Choose a spreadsheet by number: 4
    Please enter a number between 1 and 3.
    2

    Available Worksheets in Input.xlsx:
    1. 0.5mm2
    2. 10mm2
    3. 120mm2
    Choose a worksheet by number: a
    Please enter a valid number.
    2
    Cond_1_Diam_1   Unnamed: 1 Cond_1_Diam_1_1   Unnamed: 3 Cond_1_Diam_1_25   Unnamed: 5  ... Cond_0_9_Diam_1  Unnamed: 11 Cond_0_75_Diam_1  Unnamed: 13 Cond_0_5_Diam_1  Unnamed: 15
    0   Current [A]  Temp [degC]     Current [A]  Temp [degC]      Current [A]  Temp [degC]  ...     Current [A]  Temp [degC]      Current [A]  Temp [degC]     Current [A]  Temp [degC]
    1      0.155155     20.00037        0.155155    20.000356         0.155155    20.000337  ...        0.155155    20.000409         0.155155    20.000487        0.155155    20.000718
    2       0.31031    20.001392         0.31031    20.001334          0.31031    20.001257  ...         0.31031    20.001539          0.31031    20.001833         0.31031    20.002698
    3      0.465465     20.00302        0.465465     20.00289         0.465465    20.002718  ...        0.465465     20.00334         0.465465    20.003976        0.465465    20.005855
    4      0.620621    20.005233        0.620621    20.005002         0.620621    20.004697  ...        0.620621    20.005787         0.620621    20.006889        0.620621    20.010144

    [5 rows x 16 columns]
    """
    import pandas as pd
    from spreadsheets_in_folder import spreadsheets_in_folder
    from data_from_worksheet import data_from_worksheet

    # Get the dictionary of spreadsheets (keys), and underlying worksheets (list value), in the Input directory
    worksheets = spreadsheets_in_folder(folder)

    # Function to safely get the user's choice
    def get_user_choice(max_value):
        while True:
            try:
                choice = int(input())
                if 1 <= choice <= max_value:
                    return choice
                else:
                    print(f"Please enter a number between 1 and {max_value}.")
            except ValueError:
                print("Please enter a valid number.")

    # Display spreadsheets with index
    print("Available Spreadsheets:")
    for idx, file in enumerate(worksheets.keys(), 1):
        print(f"{idx}. {file}")

    # Get spreadsheet choice by index
    print("Choose a spreadsheet by number: ", end="")
    spreadsheet_idx = get_user_choice(len(worksheets)) - 1
    chosen_spreadsheet = list(worksheets.keys())[spreadsheet_idx]

    # Display worksheets with index
    print(f"\nAvailable Worksheets in {chosen_spreadsheet}:")
    for idx, sheet in enumerate(worksheets[chosen_spreadsheet], 1):
        print(f"{idx}. {sheet}")

    # Get worksheet choice by index
    print("Choose a worksheet by number: ", end="")
    worksheet_idx = get_user_choice(len(worksheets[chosen_spreadsheet])) - 1
    chosen_worksheet = worksheets[chosen_spreadsheet][worksheet_idx]
    
    # Extract data from the specific spreadsheet/worksheet
    data = data_from_worksheet(folder,chosen_spreadsheet,chosen_worksheet)

    return data

# Change this to the desired directory
folder = "D:\Python_Projects\PSS-curves\Inputs"
a = user_picked_sheet(folder)
print(a.head(5))