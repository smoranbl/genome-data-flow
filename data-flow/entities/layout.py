

class Schema:

    def __init__(self, version, level, attrs):
        self.version = version
        self.level = level
        self.attrs = attrs

    # Return a list of names that represent the schema headers.
    def get_schema_headers(self):
        return [value.name for value in self.attrs]

    # Return attribute list filtered by group
    def get_schema_headers_by_group(self, group_key):
        return [value.name for value in self.attrs if value.group == group_key]


class Attribute:

    def __init__(self, name, description, position, family, model):
        self.name = name
        self.description = description
        self.position = position
        self.family = family
        self.model = model

    # Override for return 'key: value'
    def __repr__(self):
        return self.name


class DataDictionary:
    pass
