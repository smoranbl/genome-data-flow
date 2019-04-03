
import json


def get_schema_template(version='v1.0', level='object'):
    """
    :param version: string, Version of the required schema
    :param level: string, Indicates schema type, object or field
    :return: dictionary, Schema info for passed version and level
    """
    path = '../resources/schemas/{version}/{level}_schema.json'.format(version=version, level=level)
    # Open the defined file and load json data
    with open(path) as json_file:
        schema_json = json.load(json_file)

    return schema_json['template']
