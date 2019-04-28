
import json as js

from services import google as gs


# Create a dictionary based on template version and content of table and fields
def create_data_dictionary(version_id, table_values, field_values):
    """
    :param version_id: string, identifier for data dictionary template
    :param table_values: list, result values from spreadsheet, in objects data dictionary should be just one element
    :param field_values: list, result values from spreadsheet, in field data dictionary
    :return: dict, object data dictionary
    """
    data_dictionary = dict(table=None, fields=None)

    template = select_template(version_id)
    data_dictionary['table'] = format_data_dictionary(template['table'], table_values[0])
    data_dictionary['fields'] = [format_data_dictionary(template['field'], values) for values in field_values]

    return data_dictionary


# Create a template based on version and content
def create_template_dictionary(version_id, values):
    """
    :param version_id: string, version of the legend template
    :param values: list, content of object legend template the spreadsheet
    :return: dict, template legend with the data dictionary layout for specific version
    """
    template = dict(version=version_id)

    headers = [header.lower().replace(' ', '_') for header in values.pop(0)]
    template['table'] = [format_template_dictionary(headers, value) for value in values if value[0] == 'OBJECT']
    template['field'] = [format_template_dictionary(headers, value) for value in values if value[0] == 'FIELD']

    return template


# Zip and clean the values of legend template with it's headers
def format_data_dictionary(template, values):
    """
    :param template: list, data dictionary template with corresponding layout structure
    :param values: list, data dictionary content
    :return: dict, merge of template and values to format data dictionary
    """
    data_dictionary = dict()

    for index in range(len(values)):
        item = next((item for item in template if item['order'] == index), None)
        alias = item['alias'].replace(' ', '_')

        item['value'] = values[index]
        data_dictionary[alias] = item

    return data_dictionary


# Format the template values to standardize
def format_template_dictionary(headers, values):
    """
    :param headers, list, first line of legend spreadsheet
    :param values: list, content of legend spreadsheet for sheet template
    :return: list, template formatted content
    """
    template = dict(zip(headers, values))
    del template['level']

    for key, val in template.items():
        if key == 'alias':
            template[key] = val.lower()
        elif key == 'description_en' or key == 'description_sp':
            template[key] = val.capitalize()
        elif key == 'order':
            template[key] = int(val)
        elif key == 'required':
            template[key] = True if val == 'TRUE' else False

    return template


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
    path = '../resources/templates/template-{version}.json'.format(version=version_id)

    # Open the defined file and read json data
    with open(path) as json_file:
        layout = js.load(json_file)

    return layout
