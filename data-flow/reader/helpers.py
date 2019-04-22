

# Map the values of a object data dictionary
def zip_data_dictionary(layout, object_values, field_values):
    """
    :param layout: list, data dictionary layout
    :param object_values: list, result values from spreadsheet, in objects data dictionary should be just one element
    :param field_values: list, result values from spreadsheet, in field data dictionary
    :return: dict, object data dictionary
    """
    # TODO: Is it necessary to keep key order of the dictionary?
    data_dictionary = dict(zip(layout['object_layout'], object_values[0]))
    data_dictionary['fields'] = [dict(zip(layout['field_layout'], values)) for values in field_values]

    return data_dictionary


# Map the values of legend template with it's headers
def zip_legend_template(version, object_legend_values, field_legend_values):
    """
    :param version: string, version of the legend template
    :param object_legend_values: list, content of object legend template the spreadsheet
    :param field_legend_values: list, content of field legend template the spreadsheet
    :return: dict, schema legend with the data dictionary layout for specific version
    """
    keys = ["alias", "description_en", "description_sp", "order", "required", "type", "model"]
    schema = {'version': version}

    object_legend = list(map(format_legend_template, object_legend_values))
    field_legend = list(map(format_legend_template, field_legend_values))

    print(object_legend)
    print(field_legend)

    schema['table_layout'] = [dict(zip(keys, value)) for value in object_legend]
    schema['field_layout'] = [dict(zip(keys, value)) for value in field_legend]

    return schema


# Format legend template values to standardize
def format_legend_template(values):
    """
    :param values: list, row values of legend template
    :return: list, formatted values of legend template
    """
    return [True if value == 'TRUE' else False if value == 'FALSE' else value.lower() for value in values]
