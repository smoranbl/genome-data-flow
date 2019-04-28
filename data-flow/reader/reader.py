
from reader import helpers as rh


# Load complete data dictionary from a spreadsheet
def read_data_dictionary(version_id, sheet_id):
    """
    :param version_id: string, identifier of the layout version
    :param sheet_id: string, id of the required sheet
    :return: dict, data dictionary for the specific sheet_id
    """
    # TODO: Make range generators
    table_range = 'DC-DD-Object!A3:AI'
    field_range = 'DC-DD-Field!A3:AI'

    # Extract data from spreadsheets an join it for standard Genome Work Unit
    object_values = rh.select_sheet(sheet_id, table_range)
    field_values = rh.select_sheet(sheet_id, field_range)

    return rh.create_data_dictionary(version_id, object_values, field_values)


# Load complete data dictionary from a spreadsheet
def read_legend_template(version_id, sheet_id):
    """
    :param version_id: string, identifier of the layout version
    :param sheet_id: string, id of the required sheet
    :return: dict, data dictionary for the specific sheet_id
    """
    object_legend_range = 'Object-Legend!A2:H'
    field_legend_range = 'Field-Legend!A2:H'

    object_legend_values = rh.select_sheet(sheet_id, object_legend_range)
    field_legend_values = rh.select_sheet(sheet_id, field_legend_range)

    return rh.create_template_dictionary(version_id, object_legend_values, field_legend_values)
