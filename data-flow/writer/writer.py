
import json
import os
import yaml


def write_data_dictionary(dictionary):
    path = '../resources/dictionaries/{uuaa}/{physical_name}.yaml'\
        .format(
            uuaa=dictionary['table']['uuaa']['value'],
            physical_name=dictionary['table']['physical_name']['value'])

    os.makedirs(os.path.dirname(path), exist_ok=True)
    alias_dumper = yaml.dumper.SafeDumper
    alias_dumper.ignore_aliases = lambda self, data: True

    with open(path, 'w') as out_file:
        yaml.dump(dictionary, out_file, allow_unicode=True, Dumper=alias_dumper, default_flow_style=False)


def write_template_dictionary(version, template):
    path = '../resources/templates/template-{version}.json'.format(version=version)

    with open(path, 'w') as out_file:
        json.dump(template, out_file, ensure_ascii=False, indent=4)
