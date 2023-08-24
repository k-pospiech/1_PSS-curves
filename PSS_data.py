def PSS_data():
    """
    This function takes PSS output .xls files from the Input folder and exctracts data suitable to be used with curve fitting script
    """
    import os
    import pandas as pd
    from openpyxl import load_workbook
    from spreadsheets_in_folder import spreadsheets_in_folder
    from extract_cell_data import extract_cell_data

    # Change this to the desired directory
    folder = "D:\Python_Projects\PSS-curves\Inputs"

    # Get the dictionary of spreadsheets (keys), and underlying worksheets (list value), in the Input directory
    worksheets = spreadsheets_in_folder(folder)
    # print("Detected Spreadsheets:")
    # for idx, file in enumerate(worksheets.keys(), 1):
    #     print(f"{idx}. {file}")        

    # Worksheets' names
    Worksheet_names = ['Cable selection and operating p','Temperature - current']

    # Extract columns A and B from the worksheets 
    Cable_info = {}
    Temp_v_Current = {}
    for file in worksheets:
        full_path = os.path.join(folder,file)
        Cable_info[file] = pd.read_excel(full_path,Worksheet_names[0],usecols="A,B",header=None)
        Temp_v_Current[file] = pd.read_excel(full_path,Worksheet_names[1],usecols="A,B", header=None)

    # Clean cable info data
    rows_to_del = [0, 1, 4, 6, 10, 12] + list(range(14, 19)) + list(range(20, 34))
    for key,df in Cable_info.items():
        # print(key)
        df.drop(rows_to_del, inplace=True)      # deletes obsolete rows
        df.reset_index(drop=True, inplace=True)     # resets index
        # print(Cable_info[key])
        # print("-" * 50)  # Optional line separator

    # Clean Current vs Temp data
    for key,df in Temp_v_Current.items():
        print(key)
        df.columns = ['Current [A]','Temperature [degC]']       # assigns the headers 
        df.iloc[:, 0] = df.iloc[:, 0].round(1)      # rounds the values in the Current column to one decimal place
        df.iloc[:, 1] = df.iloc[:, 1].round(2)      # rounds the values in the Temperature column to two decimal places
        print(Temp_v_Current[key])
        print("-" * 50)     # Optional line separator

    # Now we will get to simplifying the data points

    # print(Cable_info['ANSYS10mm2Copper_20230811_2305 - Copy.xls'])
    # print(Cable_info['ANSYS10mm2Copper_20230811_2305 - Copy.xls'])

    return

PSS_data()