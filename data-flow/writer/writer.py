
import json as js


def write_legend_template(legend_template):
    """
    :param legend_template:
    :return:
    """
    path = '../resources/schemas/schema-{version}.json'.format(version=legend_template['version'])

    with open(path, 'w') as schema:
        js.dump(legend_template, schema, ensure_ascii=False, indent=4)
