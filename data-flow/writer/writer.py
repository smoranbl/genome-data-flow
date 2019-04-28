
import yaml as ym


def write_data_dictionary(version, data):
    path = '../resources/schemas/schema-{version}.json'.format(version=version)

    with open(path, 'w') as file:
        ym.dump(data, file, ensure_ascii=False, indent=4)
