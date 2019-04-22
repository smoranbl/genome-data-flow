

# Map the values of a object data dictionary
def create_data_dictionary(layout, table_values, field_values):
    """
    :param layout: list, data dictionary layout
    :param table_values: list, result values from spreadsheet, in objects data dictionary should be just one element
    :param field_values: list, result values from spreadsheet, in field data dictionary
    :return: dict, object data dictionary
    """
    data_dictionary = dict()
    data_dictionary['field_dictionary'] = list()

    data_dictionary['table_dictionary'] = add_value_to_dictionary(layout['table_layout'], table_values)
    data_dictionary['field_dictionary'].append(add_value_to_dictionary(layout['field_layout'], field_values))

    return data_dictionary


def add_value_to_dictionary(layout, values):
    # TODO: Make documentation and maybe pass the second for to a function
    """
    :param layout:
    :param values:
    :return:
    """
    dictionary = list()

    # Iterate over spreadsheet data content, dictionary fields and add value to it
    for value in values:
        entity = dict()

        for index in range(len(layout)):
            entity = layout[index].copy()
            entity['value'] = value[index]

            dictionary.append(entity)

    return dictionary


# Map the values of legend template with it's headers
def create_legend_template(version, object_legend_values, field_legend_values):
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
