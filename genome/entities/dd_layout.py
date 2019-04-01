

# from handlers.file_repo import json_handler


class Schema:

    def __init__(self, level, version, attr):
        self.level = level
        self.version = version
        self.attr = attr
        self.order_schema()

    @staticmethod
    def instance_template(schema_template):
        """
        :param schema_template: list, Schema structure load from template
        :return: list[Column], Array of objects with attribute metadata load from schema template
        """
        temp_map = map(lambda c: Attribute(c['name'], c['description'], c['position'], c['group']), schema_template)

        return list(temp_map)

    # TODO: I'm not sure that copy() is necessary, need to check if schema change with a equal reference
    # Order the self.attr list based on the self.attr.position if is informed
    def order_schema(self):
        if self.attr is not None:
            sorted(self.attr, key=lambda key: key.position).copy()

    # Return a list of names that represent the schema headers.
    def get_schema_headers(self):
        return [value.name for value in self.attr]

    # Return attribute names list with formatting for cypher query
    def get_schema_query(self):
        return ','.join(map(lambda v: str(v), self.attr))


class Attribute:

    def __init__(self, name, description, position, group):
        self.name = name
        self.description = description
        self.position = position
        self.group = group

    # Override for return 'key: value'
    def __str__(self):
        return '{name}: {{{name}}}'.format(name=self.name)
