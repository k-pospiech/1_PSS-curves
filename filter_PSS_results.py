def filter_PSS_results():
    """
    Filters the PSS results from an Excel spreadsheet.

    This function reads a given worksheet in an Excel file and filters it based on
    the closest values to a range of current values from 0 to a maximum current.
    If an exact match is found for a given current, the corresponding row is
    appended to the result. Otherwise, the function calculates the average of the two
    closest rows for that current and appends it to the result.

    The resulting DataFrame is then returned, containing the filtered data.

    Parameters:
    None (Hardcoded)

    Returns:
    pandas.DataFrame: Filtered data with the same columns as the original data,
                      and the 'Current [A]' column converted to integers.
    
    Note:
    - Requires 'data_from_worksheet' function for reading the Excel worksheet.
    - Maximum current is hardcoded to 830.

    Usage Example:
    >>> filtered_data = filter_PSS_results()

    """
    from data_from_worksheet import data_from_worksheet
    import pandas as pd
    import numpy as np

    folder = "D:\Python_Projects\PSS-curves\Inputs"
    spreadsheet = "120mm2_Correlations.xlsx"
    worksheet = "Insulation_0"

    OG_data = data_from_worksheet(folder, spreadsheet, worksheet)
    
    # print(OG_data)

    # Create empty DataFrame to store the filtered results
    Filtered_data = pd.DataFrame(columns=OG_data.columns)

    # Max Current:
    max_I = 830

    for current in range(0,(max_I+1)):
        # Find rows where Current is closest to the desired value
        closest_rows = OG_data.loc[(OG_data["Current [A]"] - current).abs().argsort()[:2]]

        # Check for exact match
        if current in closest_rows["Current [A]"].values:
            Filtered_data = Filtered_data._append(closest_rows.loc[closest_rows["Current [A]"] == current])
        else:
            # Calculate the average of the two closest rows
            avg_row = pd.DataFrame(closest_rows.mean(axis=0)).transpose()
            avg_row["Current [A]"] = current #Set "Current [A] to the desired value"
            Filtered_data = pd.DataFrame._append(Filtered_data, avg_row)

    # Reset index for transparency
    Filtered_data.reset_index(drop=True, inplace=True)
    # Convert Current to integers
    Filtered_data["Current [A]"] = Filtered_data["Current [A]"].astype(int)

    # print(Filtered_data)

    return Filtered_data

a = filter_PSS_results()
# print(a.iloc[:, :1].to_string(index=False)) # Print Current column
print(a.iloc[:, -1].to_string(index=False)) # Print last (0.5 fill) column
print(a.iloc[:, 1:2].to_string(index=False)) # Print second (1 fill) column