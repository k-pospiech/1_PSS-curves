def data_from_worksheet(folder, spreadsheet, worksheet):
    """
    Extracts data from a specified worksheet within a spreadsheet file and returns it as a Pandas DataFrame.

    This function supports both Excel (.xlsx/.xls) and CSV (.csv) file formats. For Excel files, a specific
    worksheet can be specified.

    Parameters:
    - folder (str): The directory where the spreadsheet file is located.
    - spreadsheet (str): The name of the spreadsheet file, including its extension.
    - worksheet (str): The name of the worksheet within the Excel spreadsheet to read data from 
                        (not applicable for CSV files).

    Returns:
    - pd.DataFrame: A DataFrame containing the data from the specified worksheet.

    Example:
    >>> data_from_worksheet("some/directory", "spreadsheet.xlsx", "Sheet1")
    # Output would be a DataFrame containing the data from "Sheet1" in "spreadsheet.xlsx"

    Note:
    - For Excel files, both .xls and .xlsx extensions are supported.
    - For .csv files, the `worksheet` parameter is ignored.
    - Raises an error if the specified file or worksheet does not exist.
    """
    import os
    import pandas as pd

    path = os.path.join(folder,spreadsheet)

    # Two cases: .xlsx/.xls and .csv
    if spreadsheet.endswith(('.xls','.xlsx')):
        data = pd.read_excel(path,worksheet)
    elif spreadsheet.endswith('.csv'):
        data = pd.read_csv(path)

    return data