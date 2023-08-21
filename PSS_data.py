def PSS_data():
    """
    This function takes PSS output .xls files from the Input folder and exctracts data suitable to be used with curve fitting script
    """
    import pandas as pd
    from spreadsheets_in_folder import spreadsheets_in_folder

    # Get the dictionary of spreadsheets (keys), and underlying worksheets (list value), in the Input directory
    worksheets = spreadsheets_in_folder()

    for f in worksheets: 
        print(f)

    return