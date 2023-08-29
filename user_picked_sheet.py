def user_picked_sheet(folder):
    """
    Interactively allows the user to select a worksheet from spreadsheet files in a given folder to extract data.
    
    This function lists all the spreadsheet files (.xls, .xlsx, .csv) available in the provided folder. The user 
    can choose a file and a worksheet within that file by inputting the corresponding index number. The function
    returns the extracted data from the selected worksheet as a Pandas DataFrame.
    
    Error handling is in place to ensure that the user inputs a valid number for both the spreadsheet and worksheet selection.

    Parameters:
    -----------
    folder : str
        The directory path where the spreadsheet files are located.

    Returns:
    --------
    data : pd.DataFrame
        The extracted data from the chosen worksheet as a Pandas DataFrame.

    Example:
    --------
    >>> folder = "D:\\Python_Projects\\PSS-curves\\Inputs"
    >>> df = user_picked_sheet(folder)
    >>> print(df.head(5))
    [Output will display first 5 rows of the chosen worksheet's data as a Pandas DataFrame]

    User Input Example:
    -------------------
    Available Spreadsheets:
    1. File1.xls
    2. File2.xlsx
    Choose a spreadsheet by number: 2
    
    Available Worksheets in File2.xlsx:
    1. Sheet1
    2. Sheet2
    Choose a worksheet by number: 1
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