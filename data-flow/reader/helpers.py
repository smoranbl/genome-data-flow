
import json as js

from services import google as gs


# Map the values of a object data dictionary
def create_data_dictionary(version_id, table_values, field_values):
    """
    :param version_id: string, identifier for data dictionary template
    :param table_values: list, result values from spreadsheet, in objects data dictionary should be just one element
    :param field_values: list, result values from spreadsheet, in field data dictionary
    :return: dict, object data dictionary
    """
    layout = select_template(version_id)

    data_dictionary = dict()

    data_dictionary['table_dictionary'] = format_data_dictionary(layout['table_layout'], table_values)
    data_dictionary['field_dictionary'] = format_data_dictionary(layout['field_layout'], field_values)

    return data_dictionary


# Map the values of legend template with it's headers
# TODO: Revise for adapt to just one legend spreadsheet
def create_template_dictionary(version_id, object_legend_values, field_legend_values):
    """
    :param version_id: string, version of the legend template
    :param object_legend_values: list, content of object legend template the spreadsheet
    :param field_legend_values: list, content of field legend template the spreadsheet
    :return: dict, schema legend with the data dictionary layout for specific version
    """
    keys = ["alias", "description_en", "description_sp", "order", "required", "type", "model"]
    schema = {'version': version_id}

    object_legend = list(map(format_template_dictionary, object_legend_values))
    field_legend = list(map(format_template_dictionary, field_legend_values))

    schema['table_layout'] = [dict(zip(keys, value)) for value in object_legend]
    schema['field_layout'] = [dict(zip(keys, value)) for value in field_legend]

    return schema


# TODO: Make documentation and maybe pass the second for to a function
def format_data_dictionary(template, values):
    dictionary = list()

    # Iterate over spreadsheet data content and dictionary fields to add value to it
    for value in values:
        dictionary_row = list()

        for index in range(len(template)):
            alias = template[index]['alias']

            entity = dict({alias: template[index].copy()})
            entity[alias]['value'] = value[index]

            dictionary_row.append(entity)

        dictionary.append(dictionary_row)

    return dictionary


# TODO: Order value must be integer
# Format legend template values to standardize
def format_template_dictionary(values):
    """
    :param values: list, content of the legend spreadsheet for sheet template
    :return: list, template formatted content
    """
    return [True if value == 'TRUE' else False if value == 'FALSE' else value.lower() for value in values]


# Auth google sheets service and get data from defined sheet and spreadsheet range
def select_sheet(sheet_id, sheet_range):
    """
    :param sheet_id: string, id of the required sheet
    :param sheet_range: string, range definition of the required spreadsheet
    :return: list, return the content of the spreadsheet
    """
    # API call for get spreadsheet data and metadata
    values = gs.sheet_service.spreadsheets().values().get(spreadsheetId=sheet_id, range=sheet_range).execute()['values']

    return values


# Load the data dictionary template version in a Schema instance
def select_template(version_id):
    """
    :param version_id: string, version of the required schema
    :return: template, dictionary meta data info for version and level
    """
    # TODO: Maybe put layout data in sqlite catalog
    path = '../resources/schemas/schema-{version}.json'.format(version=version_id)

    # Open the defined file and read json data
    with open(path) as json_file:
        layout = js.load(json_file)

    return layout
