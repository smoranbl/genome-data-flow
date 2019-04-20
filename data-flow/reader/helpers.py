

# Map de values of a object data dictionary
def zip_object_dictionary(layout, data):
    """
    :param layout: list, data dictionary layout
    :param data: list, result values from spreadsheet, in objects dd should be just one element
    :return: dict, object data dictionary
    """
    level = layout['level']
    keys = layout['template']

    if level == 'object':
        return dict(zip(keys, data[0]))

    elif level == 'field':
        return [dict(zip(keys, values)) for values in data]
