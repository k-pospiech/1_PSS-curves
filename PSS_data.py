def PSS_data():
    """
    This function takes PSS output .xls files from the Input folder and exctracts data suitable to be used with curve fitting script
    """
    import pandas as pd
    from spreadsheets_in_folder import spreadsheets_in_folder
    from data_from_worksheet import data_from_worksheet

    # Change this to the desired directory
    folder = "D:\Python_Projects\PSS-curves\Inputs"

    # Get the dictionary of spreadsheets (keys), and underlying worksheets (list value), in the Input directory
    worksheets = spreadsheets_in_folder(folder)
    for file,sheet in worksheets.items():
        print(f"{file}: {sheet}")

    # Ask user for input which spreadsheet/worksheet they want to extract + validation
    chosen_spreadsheet = input("Spreadsheet: ")
    if chosen_spreadsheet not in worksheets:
        print("Error: Spreadsheet not found.")
        return
    chosen_worksheet = input("Worksheet: ")
    if chosen_worksheet not in worksheets[chosen_spreadsheet]:
        print("Error: Worksheet not found in the chosen spreadsheet.")
        return
    
    # Extract data from the specific spreadsheet/worksheet
    data = data_from_worksheet(folder,chosen_spreadsheet,chosen_worksheet)

    return data

a = PSS_data()
print(a.head(5))