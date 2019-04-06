

class Schema:

    def __init__(self, version, level, attrs):
        self.version = version
        self.level = level
        self.attrs = attrs

    # Return a list of names that represent the schema headers.
    def get_schema_headers(self):
        return [value.name for value in self.attrs]

    # Return attribute names list with formatting for cypher query
    def get_schema_query(self):
        return ','.join(map(lambda v: str(v), self.attrs))


class Attribute:

    def __init__(self, name, description, position, group):
        self.name = name
        self.description = description
        self.position = position
        self.group = group

    # Override for return 'key: value'
    def __repr__(self):
        return self.name
