def PSS_data():
    """
    Extracts and formats cable data from Excel files in a specified directory.

    The function reads two tables from each Excel spreadsheet in the "Inputs" folder:
    1. 'Cable selection and operating p': Information like nominal cross-section, part number, and material.
    2. 'Temperature - current': Data about temperature at different current levels.
    
    It cleans and formats the extracted data and returns two dictionaries:
    1. Temp_v_Current: Maps file names to their corresponding "Temperature - current" data as a DataFrame.
    2. Cable_info: Maps file names to their corresponding "Cable selection and operating p" data as a DataFrame.
    
    Returns:
    --------
    Temp_v_Current : dict
        A dictionary mapping the filenames to their corresponding "Temperature - current" data in a DataFrame format.
        
    Cable_info : dict
        A dictionary mapping the filenames to their corresponding "Cable selection and operating parameters" data in a DataFrame format.
        
    Example:
    --------
    >>> temp_data, cable_data = PSS_data()
    >>> print("\n", temp_data['ExampleFile.xls'])
    >>> print("\n", cable_data['ExampleFile.xls'])

        Current [A]  Temperature [degC]
    0            0.0               20.00
    1            0.2               20.00
    2            0.3               20.00
    3            0.5               20.01
    4            0.6               20.01
    ..           ...                 ...
    995        154.4              403.17
    996        154.5              403.90
    997        154.7              404.64
    998        154.8              405.38
    999        155.0              406.11

    [1000 rows x 2 columns]

                            0                   1
    0    Nominal cross section                  10
    1              Part number  ANSYS 10mm2 Copper
    2      Insulation material                 PVC
    3            Core diameter                3.57
    4           Outer diameter                3.57
    5           Filling factor               0.498
    6      Ambient temperature                20.0
    7        Operating current             155.000
    8  Voltage drop per length              1.3272
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
    Worksheet_names = ['Cable selection and operating parameters','Temperature - current']

    # Extract columns A and B from the worksheets 
    Cable_info = {}
    Temp_v_Current = {}
    for file in worksheets:
        full_path = os.path.join(folder,file)
        Cable_info[file] = pd.read_excel(full_path,Worksheet_names[0],usecols="A,B",header=None)
        Temp_v_Current[file] = pd.read_excel(full_path,Worksheet_names[1],usecols="A,B", header=None)

    # Clean cable info data
    rows_to_del = [0, 1, 4, 6, 10, 12] + list(range(14, 19)) + list(range(20, 34))
    for key, df in Cable_info.items():

        df.drop(rows_to_del, inplace=True)      # delete obsolete rows
        df.reset_index(drop=True, inplace=True)     # reset index

        # Remove the mm² from "Nominal cross section"
        df.loc[df[0] == "Nominal cross section", 1] = (
            df.loc[df[0] == "Nominal cross section", 1].str.replace(" mm²", "")
        )
        
        # Compact name
        Cable_size = df.iloc[0, 1]
        Fill_factor = df.iloc[5, 1]
        Insulation_material = df.iloc[2, 1]
        Insulation_thickness = round((float(df.iloc[4, 1]) - float(df.iloc[3, 1]))/2,2)
        # Ambient_temperature = df.iloc[6, 1]
        Name = "{}mm2_{}fill_{}_{}_thick".format(Cable_size, Fill_factor, Insulation_material, Insulation_thickness)

        # Add the name at the top of Cable_info
        Name_row = pd.DataFrame({0: ['Name'], 1: [Name]})
        df = pd.concat([Name_row, df], ignore_index=True)

        # Rename columns after all operations are done
        df.columns = ['Attribute', 'Value']

        Cable_info[key] = df

    # Clean Current vs Temp data
    for key,df in Temp_v_Current.items():
        # print(key)
        df.columns = ['Current [A]','Temperature [degC]']       # assigns the headers 
        df.iloc[:, 0] = df.iloc[:, 0].round(4)      # rounds the values in the Current column to four decimal place
        df.iloc[:, 1] = df.iloc[:, 1].round(2)      # rounds the values in the Temperature column to two decimal places
        # print(Temp_v_Current[key])
        # print("-" * 50)     # Optional line separator
        
    return Temp_v_Current, Cable_info