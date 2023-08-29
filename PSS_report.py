import os
import pandas as pd
from datetime import datetime
from PSS_data import PSS_data
from format_excel import *

def PSS_report():
    """
    Generates an Excel report from processed PSS data.

    This function retrieves data processed by PSS_data and compiles it 
    into an Excel report. The report contains separate worksheets for each 
    cable info and temperature-vs-current dataset. Each worksheet is named 
    after the specific cable's name.

    The report format is as follows:
    - Columns A and B: Temperature-vs-Current data.
    - Columns C and D: Cable-specific info.
    - Each sheet's name corresponds to the "Name" field in the Cable_info.

    The generated report is saved in the "Outputs" directory with a timestamp 
    in its filename, e.g., 'Report_2023-08-21_15-30-45.xlsx'.

    Dependencies:
        - `PSS_data`: Must be available in the same environment.
        - Modules: os, pandas, datetime

    Returns:
    None. The function saves the report directly to disk.

    Example usage:
    >>> PSS_report()
    (A new Excel file is saved in the designated "Outputs" directory.)
    """
    Temp_v_Current, Cable_info = PSS_data()
    
    # Create new output file
    Output_dir = "D:\Python_Projects\PSS-curves\Outputs"
    Date_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    File_name = os.path.join(Output_dir, ('Report_{}.xlsx'.format(Date_time)))

    # Set up the Excel writer object
    with pd.ExcelWriter(File_name, engine='xlsxwriter') as writer:

        # Loop over each key
        for key in Cable_info:
            # Extract data frames
            cable_df = Cable_info[key]
            temp_current_df = Temp_v_Current[key]
            sheet_name = Cable_info[key].iloc[0,1]
            
            # Concatenate side by side, column-wise
            combined_df = pd.concat([temp_current_df, cable_df], axis=1)

            # Write the complete data frame to new sheet in the Excel file
            combined_df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Format the excel file (adjust columns width and rows height)
    for sheet in Cable_info:
        sheet_name = Cable_info[sheet].iloc[0,1]
        format_excel(File_name, sheet_name)

    return

PSS_report()