
import json as js

from reader import helpers as rh
from services import google as gs


# Load the data dictionary template version in a Schema instance
def load_layout(version, level):
    """
    :param version: string, version of the required schema
    :param level: string, indicates schema type, object or field
    :return: template, dictionary meta data info for version and level
    """
    path = '../resources/schemas/{version}/{level}_schema.json'.format(version=version, level=level)
    # Open the defined file and load json data
    with open(path) as json_file:
        layout = js.load(json_file)

    return layout


# Auth google sheets service and get data from defined sheet and spreadsheet range
def load_sheet(service, sheet_id, sheet_range):
    """
    :param service: Service, google sheet_service
    :param sheet_id: string, id of the required sheet
    :param sheet_range: string, range definition of the required spreadsheet
    :return: list, return the content of the spreadsheet
    """
    # API call for get spreadsheet data and metadata
    values = service.spreadsheets().values().get(spreadsheetId=sheet_id, range=sheet_range).execute()['values']

    return values


# Load complete data dictionary from a spreadsheet
def load_data_dictionary(schema_version, sheet_id):
    object_range = 'DC-DD-Object!A5:AI'
    field_range = 'DC-DD-Field!A5:AI'
    service = gs.sheet_service

    object_layout = load_layout(schema_version, 'object')
    field_layout = load_layout(schema_version, 'field')

    object_values = load_sheet(service, sheet_id, object_range)
    field_values = load_sheet(service, sheet_id, field_range)

    object_dd = rh.zip_object_dictionary(object_layout, object_values)
    field_dd = rh.zip_field_dictionary(field_layout, field_values)

    object_dd['layout_version'] = schema_version
    object_dd['fields'] = field_dd

