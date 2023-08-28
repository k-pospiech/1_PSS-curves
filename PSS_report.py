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
    
    import os
    import pandas as pd
    from datetime import datetime
    from PSS_data import PSS_data

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

            # Access the XlsxWriter workbook and worksheet objects to adjust column width.
            workbook  = writer.book
            worksheet = writer.sheets[sheet_name]

            # Iterate over the columns and adjust the width based on the max length in each column.
            for idx, col in enumerate(combined_df):  # track column index and its content
                series = combined_df[col]
                max_len = max((
                    series.astype(str).map(len).max(),  # max content length
                    len(str(series.name))  # length of column name/header
                    )) + 2  # adding a little extra space
                worksheet.set_column(idx, idx, max_len)  # set column widt

    return

PSS_report()