def data_from_worksheet(folder,spreadsheet,worksheet):
    """
    Taken the directory, name of the spreadsheet, and the worksheet inside it, this function extracts the data from the inside and returns them as pandas DataFrame
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