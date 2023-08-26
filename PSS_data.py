def PSS_data():
    """
    This function takes PSS output .xls files from the Input folder and exctracts data suitable to be used with curve fitting script
    It returns string with compact name of the case, dictionary of temperature vs current, and dictionary of useful case data

    Example:
    >>> a, b, c = PSS_data()
    >>> print("\n", a, "\n\n", b['ANSYS10mm2Copper_20230811_2305 - Copy.xls'], "\n\n", c['ANSYS10mm2Copper_20230811_2305 - Copy.xls'])
 
10mm2_0.498fill_PVC_0.0_thick_20.0ambient 

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

        # Remove the mm² from "Nominal cross section"
        df.loc[df[0] == "Nominal cross section", 1] = (
        df.loc[df[0] == "Nominal cross section", 1].str.replace(" mm²", "").astype(int))
        # print(Cable_info[key])
        # print("-" * 50)  # Optional line separator

        # Compact name:
        Cable_size = df[1][0]
        Fill_factor = df[1][5]
        Insulation_material = df[1][2]
        Insulation_thickness = float(df[1][4])-float(df[1][3])
        Ambient_temperature = df[1][6]
        Name = "{}mm2_{}fill_{}_{}_thick_{}ambient".format(Cable_size,Fill_factor,Insulation_material,Insulation_thickness,Ambient_temperature)

    # Clean Current vs Temp data
    for key,df in Temp_v_Current.items():
        # print(key)
        df.columns = ['Current [A]','Temperature [degC]']       # assigns the headers 
        df.iloc[:, 0] = df.iloc[:, 0].round(1)      # rounds the values in the Current column to one decimal place
        df.iloc[:, 1] = df.iloc[:, 1].round(2)      # rounds the values in the Temperature column to two decimal places
        # print(Temp_v_Current[key])
        # print("-" * 50)     # Optional line separator
        
    return Name, Temp_v_Current, Cable_info

a, b, c = PSS_data()
print("\n", a, "\n\n", b['ANSYS10mm2Copper_20230811_2305 - Copy.xls'], "\n\n", c['ANSYS10mm2Copper_20230811_2305 - Copy.xls'])