def PSS_report():
    """
    Using the data processed by PSS_data.py, this script is creating an .xlsx report with separate worksheets, and everything gathered in one place
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

    # for file in Temp_v_Current:
    #     compelte_data = pd.concat(Temp_v_Current[file],Cable_info[file],axis=1)


    # # Alternative: Set up the writer object:
    # writer = pd.ExcelWriter(File_name, engine='openpyxl')

    # for sheet in Temp_v_Current:
    #     sheet_name = Cable_info[sheet].loc[0,1]


    #     # df.to_excel(writer, sheet_name=str(key))
    #     # writer.save()





    return Temp_v_Current, Cable_info

# Temp_v_Current, Cable_info = PSS_report()
# print("\n", Cable_info['ANSYS10mm2Copper_20230811_2305 - Copy.xls'], "\n\n", Temp_v_Current['ANSYS10mm2Copper_20230811_2305 - Copy.xls'])
# print(Cable_info['ANSYS10mm2Copper_20230811_2305 - Copy.xls'].loc[0,1])

a,b = PSS_report()
print(a['ANSYS10mm2Copper_20230811_2305 - Copy.xls'], b['ANSYS10mm2Copper_20230811_2305 - Copy.xls'])
print(b['ANSYS10mm2Copper_20230811_2305 - Copy.xls'].shape)