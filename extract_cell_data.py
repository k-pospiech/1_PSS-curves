def extract_cell_data(filepath, sheet_name, cell_address_list):
    """
    Extract data from specific cells in a worksheet.

    Parameters:
    - filepath: str -> Path to the spreadsheet.
    - sheet_name: str -> Name of the worksheet.
    - cell_address_list: List[str] -> List of cell addresses (e.g., ['A1', 'B2', 'C3']).

    Returns:
    - Dictionary with cell addresses as keys and cell values as values.

    #Example:
    >>> cell_data = extract_cell_data('path_to_your_spreadsheet.xlsx', 'Sheet1', ['A1', 'B2', 'C3'])
    >>> print(cell_data)
    """
    
    wb = load_workbook(filepath)
    ws = wb[sheet_name]
    
    data = {}
    for cell_address in cell_address_list:
        data[cell_address] = ws[cell_address].value
    
    wb.close()
    
    return data