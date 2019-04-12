

# Map the schema layout with data and create a dictionary
def get_dictionary_data(schema, data):
    dictionary_data = dict(zip(schema.get_schema_headers(), data))

    return dictionary_data


def get_labels():
    labels = [':Entity']


def filter_by_group(layout, dictionary_data):
    attributes = {k: v for k, v in dictionary_data.items() if k in layout}

    return attributes
