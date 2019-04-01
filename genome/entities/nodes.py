
class Object:

    def __init__(self, **kwargs):
        # physical attributes
        self.physical_name = kwargs.get('physical_name', None)
        self.object_type = kwargs.get('object_type', None)
        self.storage_type = kwargs.get('storage_type', None)
        self.storage_zone = kwargs.get('storage_zone', None)
        self.data_path = kwargs.get('data_path', None)
        self.uuaa = kwargs.get('UUAA', None)
        self.partitions = kwargs.get('partitions', None)
        self.schema_path = kwargs.get('schema_path', None)
        self.current_depth = kwargs.get('current_depth', None)
        # functional attributes
        self.country = kwargs.get('country', None)
        self.logical_name = kwargs.get('logical_name', None)
        self.description = kwargs.get('description', None)
        self.perimeter = kwargs.get('perimeter', None)
        self.information_level = kwargs.get('information_level', None)
        self.data_source = kwargs.get('data_source', None)
        self.type_requirement = kwargs.get('type_requirement', None)
        self.required_depth = kwargs.get('required_depth', None)
        self.estimated_volume = kwargs.get('estimated_volume', None)
        self.tags = kwargs.get('tags', None)
        # administrative attributes
        self.registration_date = kwargs.get('registration_date', None)
