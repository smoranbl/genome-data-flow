
import json as js

from reader import helpers as rh
from services import google as gs


# Load the data dictionary template version in a Schema instance
def read_layout(version):
    """
    :param version: string, version of the required schema
    :return: template, dictionary meta data info for version and level
    """
    path = '../resources/schemas/schema-{version}.json'.format(version=version)

    # Open the defined file and read json data
    with open(path) as json_file:
        layout = js.load(json_file)

    return layout


# Auth google sheets service and get data from defined sheet and spreadsheet range
def read_sheet(sheet_id, sheet_range):
    """
    :param sheet_id: string, id of the required sheet
    :param sheet_range: string, range definition of the required spreadsheet
    :return: list, return the content of the spreadsheet
    """
    # API call for get spreadsheet data and metadata
    values = gs.sheet_service.spreadsheets().values().get(spreadsheetId=sheet_id, range=sheet_range).execute()['values']

    return values


# Load complete data dictionary from a spreadsheet
def read_data_dictionary(layout_vs, sheet_id):
    """
    :param layout_vs: string, identifier of the layout version
    :param sheet_id: string, id of the required sheet
    :return: dict, data dictionary for the specific sheet_id
    """
    table_range = 'DC-DD-Object!A5:AI'
    field_range = 'DC-DD-Field!A5:AI'

    # Extract data from spreadsheets an join it for standard Genome Work Unit
    layout = read_layout(layout_vs)
    object_values = read_sheet(sheet_id, table_range)
    field_values = read_sheet(sheet_id, field_range)

    return rh.create_data_dictionary(layout, object_values, field_values)


# Load complete data dictionary from a spreadsheet
def read_legend_template(layout_vs, sheet_id):
    """
    :param layout_vs: string, identifier of the layout version
    :param sheet_id: string, id of the required sheet
    :return: dict, data dictionary for the specific sheet_id
    """
    object_legend_range = 'Object-Legend!A2:H'
    field_legend_range = 'Field-Legend!A2:H'

    object_legend_values = read_sheet(sheet_id, object_legend_range)
    field_legend_values = read_sheet(sheet_id, field_legend_range)

    return rh.create_legend_template(layout_vs, object_legend_values, field_legend_values)
