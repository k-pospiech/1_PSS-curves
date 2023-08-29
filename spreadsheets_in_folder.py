def spreadsheets_in_folder(folder):
    """
    Scans a given directory for spreadsheet files (.xls, .xlsx, .csv) and lists their worksheet names.
    
    This function scans the given folder for spreadsheet files with .xls, .xlsx, and .csv extensions.
    For each detected spreadsheet, the function lists its worksheets' names.
    For .csv files, which do not have multiple sheets, it assigns a default sheet name "Data".

    Parameters:
    -----------
    folder : str
        The path of the folder to scan for spreadsheet files.

    Returns:
    --------
    worksheets : dict
        A dictionary where keys are the names of the detected spreadsheets, and the values are lists containing 
        the names of the worksheets within each spreadsheet.

    Example:
    --------
    >>> worksheets_dict = spreadsheets_in_folder("path/to/your/folder")
    >>> print(worksheets_dict)
    {
        'ANSYS120mm2Copper_Profile.xls': ['Cable selection and operating parameters', 'Derating', 'Temperature - time', 'Voltage drop - time'], 
        'Input.xlsx': ['0.5mm2', '10mm2', '120mm2'], 
        'Template.xlsx': ['Case1', 'Case2']
    }
    """
    import os
    import xlrd
    import openpyxl

    # Define the extensions
    extensions = (".xls", ".xlsx", ".csv")

    # Get all files from the directory
    all_files = [file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder,file))]
    # Filter the spreadsheets through extensions
    spreadsheets = [check for check in all_files if check.endswith(extensions)]

    # Extract the dictionaries of sheets inside
    worksheets = {}

    for spreadsheet in spreadsheets:
        path = os.path.join(folder, spreadsheet)

        if spreadsheet.endswith(".xls"):
            wb = xlrd.open_workbook(path, on_demand=True)
            sheets = wb.sheet_names()
            wb.release_resources()
        elif spreadsheet.endswith(".xlsx"):
            wb = openpyxl.load_workbook(path, read_only=True)
            sheets = wb.sheetnames
            wb.close()
        elif spreadsheet.endswith(".csv"):
            sheets = ["Data"]

        worksheets[spreadsheet] = sheets
    
    return worksheets